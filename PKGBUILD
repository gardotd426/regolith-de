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
pkgver=1.5
pkgrel=2
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
        "${url2}"/i3xrocks_1.3.4-1_amd64.deb
        "${url2}"/i3xrocks-battery_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-cpu-usage_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-focused-window-name_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-info_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-key-indicator_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-media-player_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-memory_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-net-traffic_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-nm-vpn_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-openvpn_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-temp_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-time_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-volume_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-weather_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/i3xrocks-wifi_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/nordic_1.6.5-1ubuntu1ppa1_all.deb
        "${url2}"/plymouth-theme-regolith_1.0.3-1_all.deb
        "${url2}"/regolith-compositor-picom-glx_1.1.1-1_amd64.deb
        "${url2}"/regolith-default-settings_1.0.2-1groovy_amd64.deb
        "${url2}"/regolith-desktop-complete_2.92-1groovy_amd64.deb
        "${url2}"/regolith-ftue_1.0.11-1_amd64.deb
        "${url2}"/regolith-gdm3-theme_2.0.0-1ubuntu1~ppa1_amd64.deb
        "${url2}"/regolith-gnome-flashback_2.6.2-1_amd64.deb
        "${url2}"/regolith-i3-gaps-config_2.8.0-1_amd64.deb
        "${url2}"/regolith-i3xrocks-config_3.2.6-1ubuntu2_amd64.deb
        "${url2}"/regolith-lightdm-config_1.0.6-1_amd64.deb
        "${url2}"/regolith-look-ayu_2.6.13-1ubuntu2_amd64.deb
        "${url2}"/regolith-look-ayu-dark_2.6.13-1ubuntu2_amd64.deb
        "${url2}"/regolith-look-ayu-mirage_2.6.13-1ubuntu2_amd64.deb
        "${url2}"/regolith-look-cahuella_2.6.13-1ubuntu2_amd64.deb
        "${url2}"/regolith-look-lascaille_2.6.13-1ubuntu2_amd64.deb
        "${url2}"/regolith-look-nord_2.6.13-1ubuntu2_amd64.deb
        "${url2}"/regolith-look-pop-os_2.6.13-1ubuntu2_amd64.deb
        "${url2}"/regolith-look-solarized-dark_2.6.13-1ubuntu2_amd64.deb
        "${url2}"/regolith-look-ubuntu_2.6.13-1ubuntu2_amd64.deb
        "${url2}"/regolith-rofication_1.2.3-1_amd64.deb
        "${url2}"/regolith-rofi-config_1.3.1-1_amd64.deb
        "${url2}"/regolith-st_0.8.2-1ubuntu20ppa5_amd64.deb
        "${url2}"/regolith-styles_2.6.13-1ubuntu2_amd64.deb
        "${url2}"/regolith-system_1.4.0.4-1_amd64.deb
        "${url2}"/solarc-theme_800c997-1_amd64.deb
        "${url2}"/ubiquity-slideshow-regolith_138.5-ubuntu1~regolith1_all.deb
        "${url2}"/xrescat_1.2.1-1_amd64.deb
        flashback.patch
	i3-config.patch
        regolith-look.patch
	net-traffic.patch
)


sha256sums=(cf0d111e9bc12e163b930849105626e535550d066bac280052d83a0e4d458818
            22bbf4aaf1870963befffae41bfe7c2a0c8b674b4b0d15554a68b80a5f2429e3
            2c4060dda3ee2d3b4fc587d35a8e9c9e6e8e7cc63edf72cf1e17322b1700d902
            9fda771a69323114150a5ac95f588fe94934e5106d950037056507fc9bfc24c0
            a815480832323124dfed9ed86b8b165ad8b772f059b356b260776453c9379b85
            541a623fced10c3d8bf57beafafa3799812290155b425bbd80b89361b625d01e
            b516e814c0ae24838890880e8308a68b977079e2b9a03e215ac7188d1b69082e
            629634860542363f1374f94cc957955e699dc43b0bcf7787ebcf4794de4b16e4
            19376592345bb2c8e26c0f0bc59c2e4ab4bfc01ac87ab5eb1909d2827d28c878
            c01bb64796266cf8e403ce56c7a010c592eed8d8d38fc3c23a2687d2de742846
            8741c9aaaed980526565d7203f6e220c050a1f85faaf36609bf99257f4f661a4
            b45be919640b3b92bf94a9df47340cd18152b7686954ad8086ee379812ef89c6
            9ff4d2f7440657b2e647e1a18c562dd115624d9e782f31fca1a940983fe692e9
            e2a55c521ecf282241e9f3da8599fc91101e2cd66d488957ffd4d1d9cb853acc
            1c5106d334b5d774e35ad7b2058431b59c37a429c0650d888f2959db8f0ffce9
            f4273218dc5b0c7e724808751431b3731f86f458d48bbd9641dee9d7ee7124cc
            7cbaa1e984b0b3bce131fc81c174296c5ca24518e4b59291e12c356f74bd786c
            b835efb819461010a5afacebfe5775324212737d2fc9892842a73835eb4a0597
            b51df7aef512af41a874e47cdf9abe6748b1ecf4d22c6364355d602ce2972686
            05c66c372d378d2992ec59be553bd7de1cf0574d61313d84274f1e64bfe23d3b
            f9fabeb0442eb849a8e95163c20fbf9b40f288af0812583b270120e4d8092608
            cad27a9c659f3ded52c0aabcba9cb1ad16627bf9189e2525fecd77b8c7917254
            dcf12e6b71f8be99e7d8fda636bd5de690630e777a15f93e48442ff09add193e
            e94f0229aedd50416705209fb7000d3f0ab63dd345d5c639605926f8622ce63e
            7f500c19f6ff64a05bc13179ff8c8dff4ecc047babdad7a2f3b41a815f1b689c
            82050c4f1a95faeb4fd34eada50028f855527ffeda4277a7563a050e81f5cd02
            f8d8497b096f759797cb51c47adef958a6245e6608126db1e840097e2b3afdf5
            4f145bffa0bb044f08242a016235c12847c0de04e76bc273481a4c1e2a6d85eb
            9fc2ce3f0d2b23efa18ff81954a1843c698477ce485b7e8775502ed90ae6619e
            e6808d545b806da2e97a848c7d169a7062879482f8e165776156094e0823e552
            63bb70a12136214ff9fa94d6df93388008de55e5fb5ea69c3be426d30f5797fb
            040119e2e30f57b703f14047f52864eef72429f17551592135eb29598bef349d
            d893a5057cbb0f341e9572986c5867e8d36e7d34ccb08fe8cc8f358ec5d24e51
            dca2ae70074d27b72b1a7ecea75b1a98df9c22f7a24ac3733271911696478b71
            60e3e8d196619d3957a07d39877e9382da30f7b3c2120769e1c6b020e6a25829
            21dfeac1d5182e41a58d1b1e8a9212ffff995fe7bab021d6bf427b53d52dffe5
            c4546a2b05ffcbb7cf1f9592d2c3fe4e1c77a5fec61aea0477f9f1a7df8e9196
            5cabc1e286741923479e9a1923c2f30eed9d956fbcba0085722e5e2992e35891
            5a9b8650a114444d2e29b81357de765046eda3fceeb1a9971ca164daeb850c76
            9e957b16a5c7aa696f526d01ee6a7608321a378012ec836fbbf999938d5e6c79
            1edb890270688a337bdf6243dd1216a282210ab9a35b67cf91a4610b0df8cb85
            900c285972a9969b4d2d8bcd67dabccb817a2a77a102251d5dc1b2e254f095c8
            a162bcb533b2e7ec67800e4985b73a19728aadb0ec44ce27bc4db2b510799d02
            aab85154a0311982161cfb43c5708ed5f69aee0bcb0916e95c41a97efb5465e0
            e37fd4c1397178271479b6fb59bcb30b623c89ce13ae0d0f8ad158118ed5b763
            b84219798b644e97a473f99f9deef9e1985be1608fdbed794755dde80b694795
            ae1b03ac0d10e6f5de8ac40670caf3204f2f38f2a3a3a3d29182a2fd5740edce
	    63082efb191f31c3bc4be28f7118aa38e53b0d18b4366cbdc275a628b36876ce
	    06d1ff06149838a473191d71bd5d98f91e00ec60cdb4ee994d69f083a1233810
	    9b54d06c17b57186353a70e28c4c57eddc4ee2ca9540c62185ebcf4bac9f28e1
	    6e4c31bf1d7016cff0aa73effda3b579f674d5350c122cfa27c3aeeb19df2ae5
)




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

    extract_deb "${srcdir}"/i3xrocks_1.3.4-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-battery_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-cpu-usage_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-focused-window-name_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-key-indicator_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-media-player_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-memory_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-net-traffic_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-nm-vpn_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-openvpn_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-temp_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-time_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-volume_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-weather_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-wifi_3.2.6-1ubuntu2_amd64.deb

    patch "${pkgdir}"/usr/share/i3xrocks/net-traffic -i "${srcdir}"/net-traffic.patch
    move_copyright

}


package_regolith-styles () {
    pkgdesc="Regolith's themes for i3, gdm, gtk, rofi, plymouth, etc."
    license=('custom: GPLv3')
# FIXME    depends=("rofi" "regolith-i3" "gdm" "gtk3")

    extract_deb "${srcdir}"/ayu-theme_0.2.0-1ubuntu1~ppa1_amd64.deb
    extract_deb "${srcdir}"/cahuella_1.0.2-1_amd64.deb
    extract_deb "${srcdir}"/nordic_1.6.5-1ubuntu1ppa1_all.deb
    extract_deb "${srcdir}"/plymouth-theme-regolith_1.0.3-1_all.deb
    extract_deb "${srcdir}"/regolith-gdm3-theme_2.0.0-1ubuntu1~ppa1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-ayu_2.6.13-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/regolith-look-ayu-dark_2.6.13-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/regolith-look-ayu-mirage_2.6.13-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/regolith-look-cahuella_2.6.13-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/regolith-look-lascaille_2.6.13-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/regolith-look-nord_2.6.13-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/regolith-look-solarized-dark_2.6.13-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/regolith-look-ubuntu_2.6.13-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/regolith-look-pop-os_2.6.13-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/regolith-styles_2.6.13-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/solarc-theme_800c997-1_amd64.deb

    move_copyright
    cp "${pkgdir}"/etc/regolith/styles/ayu/typeface "${pkgdir}"/etc/regolith/styles/lascaille/typeface
    cp "${pkgdir}"/etc/regolith/styles/ayu/typeface "${pkgdir}"/etc/regolith/styles/cahuella/typeface
    patch "${pkgdir}"/usr/bin/regolith-look -i "${srcdir}"/regolith-look.patch
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

    extract_deb "${srcdir}"/regolith-compositor-picom-glx_1.1.1-1_amd64.deb
    extract_deb "${srcdir}"/regolith-default-settings_1.0.2-1groovy_amd64.deb
    extract_deb "${srcdir}"/regolith-desktop-complete_2.92-1groovy_amd64.deb
    extract_deb "${srcdir}"/regolith-ftue_1.0.11-1_amd64.deb
    extract_deb "${srcdir}"/regolith-lightdm-config_1.0.6-1_amd64.deb
    extract_deb "${srcdir}"/regolith-i3-gaps-config_2.8.0-1_amd64.deb
    extract_deb "${srcdir}"/regolith-rofi-config_1.3.1-1_amd64.deb
    extract_deb "${srcdir}"/regolith-system_1.4.0.4-1_amd64.deb
    extract_deb "${srcdir}"/ubiquity-slideshow-regolith_138.5-ubuntu1~regolith1_all.deb
    extract_deb "${srcdir}"/regolith-i3xrocks-config_3.2.6-1ubuntu2_amd64.deb
    extract_deb "${srcdir}"/regolith-rofication_1.2.3-1_amd64.deb    

    move_copyright
## extra commands
    mv "${pkgdir}"/usr/lib/python3 "${pkgdir}"/usr/lib/python3.8
    mv "${pkgdir}"/usr/lib/python3.8/dist-packages "${pkgdir}"/usr/lib/python3.8/site-packages
    rm "${pkgdir}"/usr/share/backgrounds/lucas-bellator-C0OD8OM-oM0-unsplash.jpg
    rm "${pkgdir}"/usr/share/applications/reboot.desktop
    rm "${pkgdir}"/usr/share/applications/logout.desktop
    rm "${pkgdir}"/usr/share/applications/shutdown.desktop
    sed -i 's/x-terminal-emulator/st/g' "${pkgdir}"/etc/regolith/i3/config
    patch "${pkgdir}"/etc/regolith/i3/config -i "${srcdir}"/i3-config.patch

}


package_regolith-st () {
	pkgdesc="Regolith's fork of st - the simple terminal"
	license=("MIT")
	provides=('st')
	conflicts=('st')

	extract_deb "${srcdir}"/regolith-st_0.8.2-1ubuntu20ppa5_amd64.deb

}
