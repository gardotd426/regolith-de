# Author: Matt McDonald <gardotd426@gmail.com>
# Contributor: Kevin Gilmer
# Contributor: Avinash Duduskar <strykar@hotmail.com>
# Maintainer: Matt McDonald <gardotd426@gmail.com>


pkgbase=regolith-de
pkgname=(regolith-i3 # (regolith-i3-gaps regolith-i3-gaps-session i3-gaps-wm i3-gaps-wm-dbg i3-snapshot i3xrocks gnome-flashback ubiquity-slideshow-regolith)
        regolith-i3xrocks # allll the i3xrocks shit
        regolith-styles # alll the styles shit
        regolith-st 
        regolith-desktop-config)
pkgver=1.5.3
pkgrel=1
arch=('x86_64')
url=https://github.com/regolith-linux/regolith-desktop
url2=https://launchpad.net/~regolith-linux/+archive/ubuntu/release/+files
url3=https://launchpad.net/~regolith-linux/+archive/ubuntu/unstable/+files
url4=http://archive.ubuntu.com/ubuntu/pool/main/g/gnome-session/
url5=https://launchpad.net/~regolith-linux/+archive/ubuntu/stable/+files
license=('custom: multiple')
groups=('regolith-de')
makedepends=('wget')

source=("${url2}"/ayu-theme_0.2.0-1ubuntu1~ppa1_amd64.deb
        "${url2}"/cahuella_1.0.2-1_amd64.deb
        "${url2}"/i3-snapshot_1.0-1ubuntu1~ppa1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/i/i3xrocks/i3xrocks_1.3.5-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-battery_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-cpu-usage_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-focused-window-name_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-info_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-key-indicator_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-media-player_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-memory_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-net-traffic_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-nm-vpn_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-openvpn_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-temp_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-time_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-volume_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-weather_3.5.7-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/i3xrocks-wifi_3.5.7-1_amd64.deb
        "${url2}"/nordic_1.6.5-1ubuntu1ppa1_all.deb
	"${url2}"/paper-icon-theme_1.5.723-201905252133~daily~ubuntu19.04.1_all.deb
	"${url2}"/plano-theme_3.36-1-1regolith1_all.deb
        "${url2}"/plymouth-theme-regolith_1.0.3-1_all.deb
        "${url2}"/regolith-compositor-picom-glx_1.1.3-1_amd64.deb
        "${url2}"/regolith-default-settings_1.0.5-1groovy_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-desktop/regolith-desktop-complete_2.111-1bionic_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-ftue/regolith-ftue_1.1.1-1_amd64.deb
        "${url2}"/regolith-gdm3-theme_2.0.0-1ubuntu1~ppa1_amd64.deb
        "${url2}"/regolith-gnome-flashback_2.6.2-1_amd64.deb
        "${url2}"/regolith-i3-gaps-config_2.8.4-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-i3xrocks-config/regolith-i3xrocks-config_3.5.7-1_amd64.deb
        "${url2}"/regolith-lightdm-config_1.0.6-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-styles/regolith-look-ayu_2.6.16-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-styles/regolith-look-ayu-dark_2.6.16-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-styles/regolith-look-ayu-mirage_2.6.16-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-styles/regolith-look-cahuella_2.6.16-1_amd64.deb
http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-styles/regolith-look-dracula_2.6.16-1_amd64.deb
http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-styles/regolith-look-gruvbox_2.6.16-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-styles/regolith-look-lascaille_2.6.16-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-styles/regolith-look-nord_2.6.16-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-styles/regolith-look-pop-os_2.6.16-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-styles/regolith-look-solarized-dark_2.6.16-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-styles/regolith-look-ubuntu_2.6.16-1_amd64.deb
        "${url2}"/regolith-rofication_1.3.1-1_amd64.deb
        "${url2}"/regolith-rofi-config_1.3.1-1_amd64.deb
        "${url2}"/regolith-st_0.8.2-1ubuntu20ppa5_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-styles/regolith-styles_2.6.16-1_amd64.deb
        http://ppa.launchpad.net/regolith-linux/release/ubuntu/pool/main/r/regolith-system/regolith-system_1.5.0-1_amd64.deb
        "${url2}"/solarc-theme_800c997-1_amd64.deb
        "${url2}"/ubiquity-slideshow-regolith_138.5-ubuntu1~regolith1_all.deb
        "${url2}"/xrescat_1.2.1-1_amd64.deb
        flashback.patch
	git+https://github.com/regolith-linux/regolith-rofication.git
        git+https://github.com/regolith-linux/i3xrocks.git)


sha256sums=(cf0d111e9bc12e163b930849105626e535550d066bac280052d83a0e4d458818
            22bbf4aaf1870963befffae41bfe7c2a0c8b674b4b0d15554a68b80a5f2429e3
            2c4060dda3ee2d3b4fc587d35a8e9c9e6e8e7cc63edf72cf1e17322b1700d902
            ed7b5e923a706ff10f94944ce568a49d05c0917b1ffb841ff531ed656fc2c0e6
            5c6fa9c856c05079e6050e61c871ac41d227fd24d22d4af3332b5f3fb66fade0
            5e186094552027e4d764eee9f9f3532ebb636a784ba2eacb6d2792a10b868d29
            5c18aae2a1910896f608a1a52ef31442a546278701aeb355f76d6f756d01a45b
            03fe2a42c4794a5e9b411a7395ed118b204b9cb49a8983e8d5ae990dd67831d9
            6087958e8110c29281e2a3e6743e353d06c86f0167b9e528e442944220c4c800
            8bde3af638d0cc1fd9199285ac0c06e8ccff28c563bc54b504f061dbba0527f4
            d9b115bbfe8ed62e89fde94b2adf438f17205bf5d46210906e71c5af49508d37
            f1926b37edb938f13a4b3baa25ffa011c74bcafddd85dec6b417ef60e62b7cbc
            66e2b9617aeacdd9e20e410342aa0a36705ad6b2e22467a57e3c4a5f2e4e83df
            e5b464cdd3364a6c2dd52189ad366d7ca91263ad33e0c7162f0f2b9478bf523a
            8e7394aab7d8fe0c3c12390b1b14c93884531f4727c6a3d2b8af83d12a78252d
            e53e56ba3d209a9c9347be22d352b9142da415345ab3070a14d4b00a0c062890
            2a182874228c5272a045cecde55da69e22e368e6ec0a6f35e9d8d10e308685a7
            4b3ba20a47261e93f3cd8b17aa66bc0fb9287c554d3758fb920c5e6116775355
            ef777838df1aaa7e3efa2c021f15b8ac6483ff86cd723b1c06a6df9eb0b3008c
            05c66c372d378d2992ec59be553bd7de1cf0574d61313d84274f1e64bfe23d3b
            eea3b0004671455426336e21aa285dadb2d891d1d4917f2b3ebcbcc391fe6864
            04ca38cece64a64774744325194e1b2c040a700d01439b7feb1f04eec28d82cb
            f9fabeb0442eb849a8e95163c20fbf9b40f288af0812583b270120e4d8092608
            bda06402859032215fff3b499a4d7034e3933be6eafa8473d1bb8c78aea85549
            3ad7dd8727fee27c6f0b184b85d87099b4860c1d28dbcc7e3fc62ff17a7778be
            5c381c9b76c76ed73542e9df6b8d12c89e135246c26bec09ea597145e16826ea
            561ab6caadac13ce2b77de3c5534c2eb01b47f6123c1b58fd86f8312b93135cc
            82050c4f1a95faeb4fd34eada50028f855527ffeda4277a7563a050e81f5cd02
            f8d8497b096f759797cb51c47adef958a6245e6608126db1e840097e2b3afdf5
            ec3b0387ad3f84dec9d50646c6f06ecaff8fc14353c3ea314027c2877f5081bd
            959b6ff75c74052bb49b700b6fa939d2cb1377fa2aeb064319400bf749d25c81
            e6808d545b806da2e97a848c7d169a7062879482f8e165776156094e0823e552
            8892bc8c09438b1999de2f01cd546c936e75fc470ebc52d2821b06bca46a4846
            fa6f9632a7272b790419e54d33000550c2e8fc8a30a27ba8841d967736e03f85
            69faab5c04fff978fc0982e89679aec359601790ca70f827285a4acbce6d4669
            4936fd53a87b776761d45a756ebc2b4ae1dd5cd7ce0b91ef7277d8d15f1196e4
            52b290af0c5aa28a357f19d124223202419916a3f3b41b13100480b10c84308f
            8e6b6c7250c7cecfebe101fc02538841a381e150d3b5d409cb87d73bc48ee043
            eac9ce8ba05892ca82f5c708bed9dfd2c5bca52b97d62dd26a9a11af42bf0f01
            c834965df1fd23da9a7fb09ad6bda2042e02cee2be0dea62d5365eebf9191d3c
            7263a465778d97cd2e3ecfa3082567db5d3e7742a7bfaada7554b2e4ef9e9a2c
            e1c7f1c3b6cb66d63fabc5af804424c46c49a89b056930b918ef996646f95c4c
            9c620020e7e9bb3c28df70678924cec8ace6e442d4314d1c2b595bb566d01387
            a05906dff1fa4844b9f54a7f048379011c2b93ca56e90434257a5c469debe5a6
            1edb890270688a337bdf6243dd1216a282210ab9a35b67cf91a4610b0df8cb85
            900c285972a9969b4d2d8bcd67dabccb817a2a77a102251d5dc1b2e254f095c8
            7ecee3e774b5178dcf125aa32a8fedecc4c69abc868abe1fcc88c96693bcacef
            15ccd5d02c73b2f42153ad074365a27e906bbfd32a11d68e181035b8e4ebf67f
            e37fd4c1397178271479b6fb59bcb30b623c89ce13ae0d0f8ad158118ed5b763
	    b84219798b644e97a473f99f9deef9e1985be1608fdbed794755dde80b694795
	    ae1b03ac0d10e6f5de8ac40670caf3204f2f38f2a3a3a3d29182a2fd5740edce
	    63082efb191f31c3bc4be28f7118aa38e53b0d18b4366cbdc275a628b36876ce
	    'SKIP'
	    'SKIP')




PKGEXT=".pkg.tar"


# extracts a debian package
# $1: deb file to extract
extract_deb() {
    local tmpdir="$(basename "${1%.deb}")"
    rm -Rf "$tmpdir"
    mkdir "$tmpdir"
    cd "$tmpdir"
    ar x "$1"
    tar -C "${pkgdir}" -xf data.tar.xz
}
# move ubuntu specific /usr/lib/x86_64-linux-gnu to /usr/lib
# $1: debian package library dir (from x86_64 or i386)
# $2: arch package library dir (goes to usr/lib or usr/lib32)
move_libdir() {
    local deb_libdir="$1"
    local arch_libdir="$2"

    if [ -d "${pkgdir}/${deb_libdir}" ]; then
        if [ ! -d "${pkgdir}/${arch_libdir}" ]; then
            mkdir -p "${pkgdir}/${arch_libdir}"
        fi
        mv -t "${pkgdir}/${arch_libdir}/" "${pkgdir}/${deb_libdir}"/*
        find ${pkgdir} -type d -empty -delete
    fi
}
# move copyright file to proper place and remove debian changelog
move_copyright() {
    find ${pkgdir}/usr/share/doc -name "changelog.Debian.gz" -delete
    mkdir -p ${pkgdir}/usr/share/licenses/${pkgname}
    find ${pkgdir}/usr/share/doc -name "copyright" -exec mv {} ${pkgdir}/usr/share/licenses/${pkgname} \;
    find ${pkgdir}/usr/share/doc -type d -empty -delete
}

build () {
    cd "${srcdir}"/regolith-rofication
    python setup.py build
    cd "${srcdir}"/i3xrocks/
}




package_regolith-i3 () {
    pkgdesc="Regolith's i3-gaps-based DE's underpinnings and gnome foundational dependencies"
    license=('MIT')
    arch=('x86_64')
    depends=('i3-gaps' 'i3status' 'xorg-server-common' 'xorg-server-devel' 'xcb-util-keysyms'  'xcb-util-wm'  'libev'  
             'yajl'  'startup-notification'  'pango'  'perl' 'xorg-server'
             'xcb-util-xrm'  'libxkbcommon-x11' 'python-i3ipc' 'gnome-flashback' 
             'accountsservice' 'cups-pk-helper' 'libgtop' 'gnome-control-center' 'gnome-desktop' 
	     'xorg-xwininfo' 'dbus' 'python-gobject' 'python-dbus' 'xorg-xprop' 'libev' 'pcre'
	     'libconfig' 'xcb-util-image' 'xcb-util-renderutil' 'libsigc++' 'gnome-session'
             'gnome-settings-daemon' 'playerctl')
    optdepends=('picom: For compositing/desktop effects - strongly recommended!'
		'unclutter-xfixes-git: For unclutter'
		'lightdm: Display Manager - Regolith LightDM theme included in regolith-desktop-config' )
    provides=('i3-snapshot' 'xrescat' 'regolith-gnome-flashback')
    conflicts=()

    extract_deb "${srcdir}"/i3-snapshot_1.0-1ubuntu1~ppa1_amd64.deb
    extract_deb "${srcdir}"/regolith-gnome-flashback_2.6.2-1_amd64.deb
    extract_deb "${srcdir}"/xrescat_1.2.1-1_amd64.deb
    
    # extra command
    patch "${pkgdir}"/usr/bin/regolith-session -i "${srcdir}"/flashback.patch

    move_copyright
}

package_i3-snapshot () {
    pkdesc="Save and restore window and workspace layout within an i3wm instance. Alternative to i3-save-tree from Regolith Linux"
    license=('BSD-3-Clause')
    arch=('x86_64')
    depends=('i3' 'jsoncpp' 'libsigc++')
    provides=('i3-snapshot')

    extract_deb "${srcdir}"/i3-snapshot_1.0-1ubuntu1~ppa1_amd64.deb

    move_copyright
}

package_regolith-i3xrocks () {
    pkgdesc="Regolith's i3xrocks with associated widgets and config files"
    license=('GPLv3')
    arch=('x86_64')
    depends=('glibc' 'accountsservice' 'alsa-utils' 'bc' 'ttf-font-awesome')
    conflicts=('i3xrocks')
    provides=('i3xrocks')

 #   extract_deb "${srcdir}"/i3xrocks_1.3.5-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-battery_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-cpu-usage_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-focused-window-name_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-info_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-key-indicator_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-media-player_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-memory_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-net-traffic_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-nm-vpn_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-openvpn_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-temp_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-time_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-volume_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-weather_3.5.7-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-wifi_3.5.7-1_amd64.deb
    cd "${srcdir}"/i3xrocks/
#    ./autogen.sh
#    ./configure 
#    make && sed -i 's+}/bin+}/usr/bin+g' configure 
#    make prefix=$pkgdir/ install
    ./autogen.sh
    ./configure --prefix=$pkgdir/
    make && make datarootdir=$pkgdir/usr/share exec_prefix=$pkgdir/usr install

    move_copyright

}


package_regolith-styles () {
    pkgdesc="Regolith's themes for i3, gdm, gtk, rofi, plymouth, etc."
    license=('custom: GPLv3')
    depends=("regolith-i3" "gtk3" "ttf-jetbrains-mono")
    conflicts=("paper-icon-theme" "nordic-theme-git" "gtk-theme-solarc-git" "gtk-theme-plano" "gtk-theme-plano-git")
    provides=("paper-icon-theme" "regolith-styles" "regolith-look" "gtk-theme-solarc" "gtk-theme-plano")

    extract_deb "${srcdir}"/ayu-theme_0.2.0-1ubuntu1~ppa1_amd64.deb
    extract_deb "${srcdir}"/cahuella_1.0.2-1_amd64.deb
    extract_deb "${srcdir}"/nordic_1.6.5-1ubuntu1ppa1_all.deb
    extract_deb "${srcdir}"/paper-icon-theme_1.5.723-201905252133~daily~ubuntu19.04.1_all.deb
    extract_deb "${srcdir}"/plano-theme_3.36-1-1regolith1_all.deb
    extract_deb "${srcdir}"/plymouth-theme-regolith_1.0.3-1_all.deb
    extract_deb "${srcdir}"/regolith-gdm3-theme_2.0.0-1ubuntu1~ppa1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-ayu_2.6.16-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-ayu-dark_2.6.16-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-ayu-mirage_2.6.16-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-cahuella_2.6.16-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-dracula_2.6.16-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-gruvbox_2.6.16-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-lascaille_2.6.16-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-nord_2.6.16-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-pop-os_2.6.16-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-solarized-dark_2.6.16-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-ubuntu_2.6.16-1_amd64.deb
    extract_deb "${srcdir}"/regolith-styles_2.6.16-1_amd64.deb
    extract_deb "${srcdir}"/solarc-theme_800c997-1_amd64.deb

    move_copyright
    cp "${pkgdir}"/etc/regolith/styles/ayu/typeface "${pkgdir}"/etc/regolith/styles/lascaille/typeface
    cp "${pkgdir}"/etc/regolith/styles/ayu/typeface "${pkgdir}"/etc/regolith/styles/cahuella/typeface
}

package_regolith-desktop-config () {
    pkgdesc="Regolith DE's desktop settings and configuration files, for rofi, i3, lightdm, i3xrocks, etc. plus ubiquity-slideshow-regolith"
    license=('Custom')
    provides=('regolith-ftue' 'regolith-rofication')
    depends=('rofi' 'adobe-source-code-pro-fonts')
    optdepends=('lightdm: For the Regolith LightDM customization' 
		'regolith-i3xrocks: For i3xrocks (i3blocks) support'
	        'i3-gaps: For i3-gaps config support'
		'picom: For compositing configuration')

    extract_deb "${srcdir}"/regolith-compositor-picom-glx_1.1.3-1_amd64.deb
    extract_deb "${srcdir}"/regolith-default-settings_1.0.5-1groovy_amd64.deb
    extract_deb "${srcdir}"/regolith-desktop-complete_2.111-1bionic_amd64.deb
    extract_deb "${srcdir}"/regolith-ftue_1.1.1-1_amd64.deb
    extract_deb "${srcdir}"/regolith-lightdm-config_1.0.6-1_amd64.deb
    extract_deb "${srcdir}"/regolith-i3-gaps-config_2.8.4-1_amd64.deb
    extract_deb "${srcdir}"/regolith-rofi-config_1.3.1-1_amd64.deb
    extract_deb "${srcdir}"/regolith-system_1.5.0-1_amd64.deb
    extract_deb "${srcdir}"/ubiquity-slideshow-regolith_138.5-ubuntu1~regolith1_all.deb
    extract_deb "${srcdir}"/regolith-i3xrocks-config_3.5.7-1_amd64.deb

    move_copyright
## extra commands
    rm "${pkgdir}"/usr/share/backgrounds/lucas-bellator-C0OD8OM-oM0-unsplash.jpg
    rm "${pkgdir}"/usr/share/applications/reboot.desktop
    rm "${pkgdir}"/usr/share/applications/logout.desktop
    rm "${pkgdir}"/usr/share/applications/shutdown.desktop
    sed -i 's/x-terminal-emulator/st/g' "${pkgdir}"/etc/regolith/i3/config
    cd "${srcdir}"/regolith-rofication
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
    install -Dm644 "${srcdir}"/regolith-rofication/80_rofication "${pkgdir}"/etc/regolith/i3xrocks/conf.d/
}


package_regolith-st () {
	pkgdesc="Regolith's fork of st - the simple terminal"
	license=("MIT")
	provides=('st')
	conflicts=('st')

	extract_deb "${srcdir}"/regolith-st_0.8.2-1ubuntu20ppa5_amd64.deb
}
