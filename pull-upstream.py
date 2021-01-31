#!/usr/bin/env python3

from datetime import date, datetime
import os.path
import pdb
import pickle
import re
import subprocess

from bs4 import BeautifulSoup
import click
from loguru import logger
import requests

##
## CONFIGURABLES
## No need to edit this, just pass args.
##

DEFAULT_CHAN="release" # also valid: unstable, stable
DEFAULT_ARCH="amd64" # in Ubuntu's terms ; not Arch's

PKG_DATA_PICKLE_PATH="upstream_pkg_data.pickle"

##
## END OF CONFIGURABLES
##

def get_in(d, ks):
    """Get a value from arbitrarily nested dicts"""
    if not ks:
        return d
    elif len(ks) == 1:
        return d.get(ks[0])
    else:
        return get_in(d.get(keys[0], {}), keys[1:])


def http_get_or_die(uri):
    res = requests.get(uri)
    if res.status_code != 200:
        exit(f"error {res.status_code} fetching '{uri}'")
    return BeautifulSoup(res.text, features="html.parser")


_ABSOLUTE_URI_RE=re.compile("^(https?:)?//") # yucki but good enough for launchpad in early 2021
def crawl_upstream_page(uri):
    logger.info(f"Fetching {uri}")
    page = http_get_or_die(uri)
    result = {}

    # Crawl descending directories
    dir_imgs = page.select("IMG[alt='[DIR]']")
    for dir_img in dir_imgs:
        a_elements = dir_img.parent.parent.select("a")
        href = a_elements[0]["href"]
        assert(not _ABSOLUTE_URI_RE.match(href))
        child_uri = uri + href
        result.update(crawl_upstream_page(child_uri))

    # Look for archives
    file_imgs = page.select("IMG[alt='[   ]']")
    for file_img in file_imgs:
        a_elements = file_img.parent.parent.select("a")
        href = a_elements[0]["href"]
        assert(not _ABSOLUTE_URI_RE.match(href))
        result[href] = uri + href

    if len(file_imgs) > 0:
        logger.info(f"Added {len(file_imgs)} files")

    return result


def crawl_upstream(main_uri):
    logger.info(f"Starting upstream crawl from {main_uri}")
    pkg_data = crawl_upstream_page(main_uri)

    if os.path.exists(PKG_DATA_PICKLE_PATH):
        # Make sure we create a new file so that ctime is properly set
        os.remove(PKG_DATA_PICKLE_PATH)

    with open(PKG_DATA_PICKLE_PATH, 'wb') as f:
        pickle.dump(pkg_data, f)

    logger.success(f"Wrote upstream pkg data to {PKG_DATA_PICKLE_PATH}")
    return pkg_data


def get_package_list(main_uri, force_crawl):
    if os.path.exists(PKG_DATA_PICKLE_PATH) and not force_crawl:
        ctime_ts = os.stat(PKG_DATA_PICKLE_PATH).st_ctime
        pickle_age = datetime.now() - datetime.fromtimestamp(ctime_ts)
        if pickle_age.days > 7: # older than a week
            logger.warning(f"Loading {pickle_age.days} days old pickled pkg data" +
                           f"from {PKG_DATA_PICKLE_PATH}. 'rm' it to fetch fresher data.")
        else:
            logger.info(f"Loading pickled pkg data from {PKG_DATA_PICKLE_PATH}")

        with open(PKG_DATA_PICKLE_PATH, 'rb') as f:
            pkgs = pickle.load(f)

        logger.success("Done loading")
    else:
        pkgs = crawl_upstream(main_uri)

    return pkgs


_PKG_NAME_RE = re.compile("(?:.*/)?([^_]+)_([^_]+)_([^.]+)\.deb")
def pkg_name_parser(pkgname, extra_data={}):
    m = _PKG_NAME_RE.match(pkgname)
    if m:
        result = {"name": m[1], "version": m[2], "arch": m[3], "filename": pkgname}
    else:
        result = {"url": pkgname, "mismatch": True}
    result.update(extra_data)
    return result


def pkgbuild_load():
    with open("PKGBUILD", "r") as f:
        lines = f.readlines()
    return lines


def pkgbuild_end_eval(shell_src):
    # I wrote a stupid parser that was OK parsing current PKGBUILD, but fairly brittle.
    # And then I thought ... what parses a PKGBUILD really well?
    # Oh yes, an actual shell. Like bash.
    #
    # And because this PKGBUILD has zero top level commands (yay!), something like
    #
    #     sh$ echo '${source[@]}' | cat PKGBUILD - | bash
    #
    # works just file, and prints a very easy to parse space separated source list.
    result = subprocess.run(f"echo '{shell_src}' | cat PKGBUILD - | bash -s",
                            capture_output=True, shell=True, text=True, check=True)
    return result


def pkgbuild_parse(pkgbuild_lines):
    src_result = pkgbuild_end_eval("echo ${source[@]}")
    sha_result = pkgbuild_end_eval("echo ${sha256sums[@]}")

    pkg_lines = src_result.stdout.split()
    pkg_dicts = [pkg_name_parser(line, {"idx": i}) for i, line in enumerate(pkg_lines)]
    pkg_data = {pkg_dict["name"]: pkg_dict for pkg_dict in pkg_dicts if "name" in pkg_dict}

    sha_lines = sha_result.stdout.split()
    for datum in pkg_data.values():
        datum["sha256"] = sha_lines[datum["idx"]]

    return pkg_data


# Dodging version compares by just patching in upstream versions for anything we got.
#
# semver_re = regexp.compile(...)
# def version_gt(a, b):
#     """True if a is more recent than b, False otherwise."""


_SOURCE_PREFIX="source=("
def pkgbuild_patch_pkg(pkgbuild_lines, pkgbuild_pkg, upstream_pkg):
    cur_name = pkgbuild_pkg['name']
    ups_name = upstream_pkg['name']
    assert(cur_name == ups_name)

    cur_vers = pkgbuild_pkg['version']
    ups_vers = upstream_pkg['version']
    assert(cur_vers != ups_vers)

    logger.info(f"Upgrading {cur_name} from current {cur_vers} to {ups_vers}")

    # Hunt for our package in PKGBUILD lines
    # XXX name and vers should be regexp-escaped
    line_re = re.compile('( *)("[^"]+"/)' + f"({cur_name}_{cur_vers}.*)")
    line_re_2 = re.compile('( *)(.*/)' + f"({cur_name}_{cur_vers}.*)")
    matches = [(i, line_re.match(l) or line_re_2.match(l)) for i, l in enumerate(pkgbuild_lines)]
    matches = [(i, m) for i, m in matches if m]

    if len(matches) != 2:
        logger.error(f"Found {len(matches)} matches for {cur_name}_{cur_vers} in PKGBUILD. Not patching.")
        return pkgbuild_lines, False

    new_lines = pkgbuild_lines.copy()
    for line, match in matches:
        if "srcdir" in match[0]:
            # Keep variable expansion for local files
            new_line = match[1] + match[2] + upstream_pkg["filename"]
        else:
            # Rebuild patched line, keeping prefix, discarding in-PKGBUILD variables expansions
            # to keep it 'simple'
            new_line = match[1] + upstream_pkg["url"]

        # Rebuild patched PKGBUILD lines
        new_lines[line] = f"{new_line}\n"

    return new_lines, True


def pkgbuild_update(pkgbuild_lines, pkgbuild_pkgs, upstream_pkgs):
    to_rehash_pkgs = []

    for name, pkgbuild_pkg in pkgbuild_pkgs.items():
        if name not in upstream_pkgs:
            # XXX the script should be able to remove these
            logger.warning(f"Package {name} was not found while crawling upstream. Ignoring.")
            continue

        upstream_pkg = upstream_pkgs[name]
        if upstream_pkg["version"] != pkgbuild_pkg["version"]:
            pkgbuild_lines, patched = pkgbuild_patch_pkg(pkgbuild_lines, pkgbuild_pkg, upstream_pkg)
            if patched:
                to_rehash_pkgs.append((pkgbuild_pkg, upstream_pkg))
        else:
            logger.debug(f"Keeping {name} at version {pkgbuild_pkg['version']}")

    return pkgbuild_lines, to_rehash_pkgs


def rehash_pkgs(to_rehash_pkgs):
    rehashes = []

    for pkgbuild_pkg, upstream_pkg in to_rehash_pkgs:
        url = upstream_pkg["url"]
        filename = upstream_pkg["filename"]

        # XXX support force download
        if os.path.exists(filename):
            logger.info(f"Using local copy of {filename} - download skipped")
        else:
            logger.info(f"Downloading {url}")
            response = requests.get(url)
            if response.status_code != 200:
                logger.error(f"Problem fetching {url} ; {response}")
                continue

            with open(upstream_pkg["filename"], "wb") as f:
                f.write(response.content)

        # Just run sha256sum as a subprocess, which is likely to be faster than any pure Python
        # implem. Maybe going with a CPython extension would be ~faster, but I cba to select an
        # additional dependency.
        result = subprocess.run(["sha256sum", filename], capture_output=True, text=True, check=True)
        sha256 = result.stdout.split()[0]
        rehashes.append((pkgbuild_pkg['sha256'], sha256))

    return rehashes


def pkgbuild_update_hashes(pkgbuild_lines, rehashes):
    new_lines = []
    rehash_set = set(rehashes)
    for i, line in enumerate(pkgbuild_lines):
        to_remove = None
        new_line = None
        for rehash_tuple in rehash_set:
            rehash_from, rehash_to = rehash_tuple
            if rehash_from in line:
                new_line = line.replace(rehash_from, rehash_to)
                to_remove = rehash_tuple
                # XXX is it safe to break here? (not if one SHA256 be present several times)
        new_lines.append(new_line if new_line else line)
        if to_remove:
            rehash_set.remove(to_remove) # Gradually decrease the inner loop iteration count
    return new_lines


# _UBUNTU_VERSION_RE=re.compile(r"""
#         ^(?P<maj>[0-9]+)\.      # Upstream Major
#         (?P<min>[0-9]+)\.       # Upstream Minor
#         (?P<pat>[0-9]+)-        # Upstream Patch
#         (?P<tag>[0-9]+)         # Ubuntu Patchlevel
#         (?P<rls>[a-z]+)?        # Ubuntu Releasename
#         (?P<end>~.*)?$           # Ubuntu ~whatever at the end
# """, re.VERBOSE)
#
#
# _UBUNTU_RELEASE_NAMES = dict(zesty=1704, artful=1710, bionic=1804, cosmic=1810, disco=1904,
#                              eoan=1910, focal=2004, groovy=2010, hirsute=2104)
#
#
# class UbuntuVersion:
#     def __init__(self, version_string):
#         self.s = version_string
#         self.m = _UBUNTU_VERSION_RE.match(version_string)
#         assert(self.m)
#     def __lt__(self, other):
#         pass
#     def __gt__(self, other):
#         pass
#     def __eq__(self, other):
#         return self.s == other.s
#     def __le__(self, other):
#         return self.__lt__(self, other) or self.__eq__(self, other)
#     def __ge__(self, other):
#         return self.__gt__(self, other) or self.__eq__(self, other)
#     def __ne__(self, other):
#         return not self.__eq__(self, other)


def filter_crawled_pkgs(upstream_names_to_urls, arch):
    # Parse all names into dicts
    parsed_pkgs = [pkg_name_parser(name, {"url": url}) for name, url in upstream_names_to_urls.items()]

    # Filter mis-parsed and wrong archs packages
    filter_fn = lambda p: "mismatch" not in p and (p["arch"] == arch or p["arch"] == "all")
    filtered_pkgs = [pkg for pkg in parsed_pkgs if filter_fn(pkg)]

    # Index back all packages into a dict ; names to upstream versions (plural)
    indexed_pkgs = {}
    for pkg in filtered_pkgs:
        name = pkg["name"]
        if name not in indexed_pkgs:
            indexed_pkgs[name] = [pkg]
        else:
            indexed_pkgs[name].append(pkg)

    # Select the version we're interested in ; for cases with several upstream versions
    result = {}
    for name, pkgs in indexed_pkgs.items():
        if len(pkgs) == 1:
            result[name] = pkgs[0]
        else:
            # 'Highest' version in lexicographical order wins
            vs = sorted(pkgs, key=lambda x: x["version"])
            result[name] = vs[-1]

    return result


@click.command()
@click.option("-a", "--arch", default=DEFAULT_ARCH, help=f"Any upstream supported arch (default {DEFAULT_ARCH})")
@click.option("-c", "--chan", default=DEFAULT_CHAN, help=f"unstable|stable|release (default {DEFAULT_CHAN})")
@click.option("-f", "--force/--no-force", default=False, help=f"Don't reuse saved crawl data if present")
def main(arch, chan, force):
    """
    Helper script to update regolith-de PKGBUILD.

    This was written to ease the maintainer's life, and for adventurous people willing to
    break their system in the name of progress.

    With it, you can get packages not made for amd64, or get some of the stable/unstable
    packages versions that are not pushed in the repo.
    """
    main_uri=f"http://ppa.launchpad.net/regolith-linux/{chan}/ubuntu/pool/main/"

    upstream_names_to_urls = get_package_list(main_uri, force)
    upstream_pkgs = filter_crawled_pkgs(upstream_names_to_urls, arch)

    pkgbuild_lines = pkgbuild_load()
    pkgbuild_pkgs = pkgbuild_parse(pkgbuild_lines)

    updated_pkgbuild_lines, to_rehash_pkgs = pkgbuild_update(pkgbuild_lines, pkgbuild_pkgs, upstream_pkgs)
    pkg_rehashes = rehash_pkgs(to_rehash_pkgs)
    updated_pkgbuild_lines = pkgbuild_update_hashes(updated_pkgbuild_lines, pkg_rehashes)

    with open("PKGBUILD.new", "w") as f:
        f.writelines(updated_pkgbuild_lines)
    logger.success("Wrote PKGBUILD.new - Please diff then copy over if satisfied.")


if __name__ == "__main__":
    main()
