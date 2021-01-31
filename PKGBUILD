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
        "${url2}"/i3xrocks-battery_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-cpu-usage_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-focused-window-name_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-info_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-key-indicator_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-media-player_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-memory_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-net-traffic_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-nm-vpn_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-openvpn_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-temp_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-time_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-volume_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-weather_3.5.6-1_amd64.deb
        "${url2}"/i3xrocks-wifi_3.5.6-1_amd64.deb
        "${url2}"/nordic_1.6.5-1ubuntu1ppa1_all.deb
	"${url2}"/paper-icon-theme_1.5.723-201905252133~daily~ubuntu19.04.1_all.deb
	"${url2}"/plano-theme_3.36-1-1regolith1_all.deb
        "${url2}"/plymouth-theme-regolith_1.0.3-1_all.deb
        "${url2}"/regolith-compositor-picom-glx_1.1.3-1_amd64.deb
        "${url2}"/regolith-default-settings_1.0.5-1groovy_amd64.deb
        "${url2}"/regolith-desktop-complete_2.106-1groovy_amd64.deb
        "${url2}"/regolith-ftue_1.0.11-1_amd64.deb
        "${url2}"/regolith-gdm3-theme_2.0.0-1ubuntu1~ppa1_amd64.deb
        "${url2}"/regolith-gnome-flashback_2.6.2-1_amd64.deb
        "${url2}"/regolith-i3-gaps-config_2.8.4-1_amd64.deb
        "${url2}"/regolith-i3xrocks-config_3.5.6-1_amd64.deb
        "${url2}"/regolith-lightdm-config_1.0.6-1_amd64.deb
        "${url2}"/regolith-look-ayu_2.6.14-1_amd64.deb
        "${url2}"/regolith-look-ayu-dark_2.6.14-1_amd64.deb
        "${url2}"/regolith-look-ayu-mirage_2.6.14-1_amd64.deb
        "${url2}"/regolith-look-cahuella_2.6.14-1_amd64.deb
	"${url2}"/regolith-look-dracula_2.6.14-1_amd64.deb
	"${url2}"/regolith-look-gruvbox_2.6.14-1_amd64.deb
        "${url2}"/regolith-look-lascaille_2.6.14-1_amd64.deb
        "${url2}"/regolith-look-nord_2.6.14-1_amd64.deb
        "${url2}"/regolith-look-pop-os_2.6.14-1_amd64.deb
        "${url2}"/regolith-look-solarized-dark_2.6.14-1_amd64.deb
        "${url2}"/regolith-look-ubuntu_2.6.14-1_amd64.deb
        "${url2}"/regolith-rofication_1.3.1-1_amd64.deb
        "${url2}"/regolith-rofi-config_1.3.1-1_amd64.deb
        "${url2}"/regolith-st_0.8.2-1ubuntu20ppa5_amd64.deb
        "${url2}"/regolith-styles_2.6.14-1_amd64.deb
        "${url2}"/regolith-system_1.4.0.4-1_amd64.deb
        "${url2}"/solarc-theme_800c997-1_amd64.deb
        "${url2}"/ubiquity-slideshow-regolith_138.5-ubuntu1~regolith1_all.deb
        "${url2}"/xrescat_1.2.1-1_amd64.deb
        flashback.patch
)


sha256sums=(cf0d111e9bc12e163b930849105626e535550d066bac280052d83a0e4d458818
            22bbf4aaf1870963befffae41bfe7c2a0c8b674b4b0d15554a68b80a5f2429e3
            2c4060dda3ee2d3b4fc587d35a8e9c9e6e8e7cc63edf72cf1e17322b1700d902
            9fda771a69323114150a5ac95f588fe94934e5106d950037056507fc9bfc24c0
            5826044bdb2dd01fff3c0e32f607fd422cdf1a7595a51d1dc598cf3af4cc536e
            9a5d35908e90ea711b1168d1a3c594c2040601852ef54aa34685043405fe75f2
            40e75d5d70ce8eb529765b55baad88d91fee8df80e37d78658547576df65c86d
            ec00973419662aadd83b612f92e1def87bc473a296b58ff8691d64ebf2ac1042
            25cd4d63004453ccb1f838036c26a8a956e27f2093eebba3c82c72552c3f88be
            f77498aa17ba4b0d961c235a61015b5cfddf1365bcddc3fb213f8a0c67ae4ca5
            bab437c7a181c3fed97e2afa599581d2afb618cf40ab382076b3c3f27138f8e7
            4e6ad8a35b5c066c1e240c8371092ba9f3b35e16c66c2d5e56ebcab8d18824dd
            c0b2df8461daec9ea294b10e69d1fea8d0bc637da5e353027dfcc31a26644581
            8f890bbfcaf8c3e92cab579e669f27fce931b24d1f4223bb2acf5c58a21a88df
            4a30f8b9d2a9b7826dc95f12ecf9cdf574d985f59510e432e73ab216b99532ee
            aff36fadd95990f463cfbe6974382f65d341b7a81fce51238dbcf56a2630ad2d
            c5fb7658092283027a106bd5c342121c76f50845d684f720085bd1c5fa96cba9
            9811bb89bc2c1721769e560459add1766ca271ac8eea3a6711ba9df224cbff8d
            c31f04a809a673cc8daf4656656c7ee9d097278001570f90c2dcb9cd054b08e1
            05c66c372d378d2992ec59be553bd7de1cf0574d61313d84274f1e64bfe23d3b
            eea3b0004671455426336e21aa285dadb2d891d1d4917f2b3ebcbcc391fe6864
            04ca38cece64a64774744325194e1b2c040a700d01439b7feb1f04eec28d82cb
            f9fabeb0442eb849a8e95163c20fbf9b40f288af0812583b270120e4d8092608
            bda06402859032215fff3b499a4d7034e3933be6eafa8473d1bb8c78aea85549
            3ad7dd8727fee27c6f0b184b85d87099b4860c1d28dbcc7e3fc62ff17a7778be
            88725f230d5d4aab0a7c6f51787fe507ce4d6224daf9e7b95499bf0707743d4b
            7f500c19f6ff64a05bc13179ff8c8dff4ecc047babdad7a2f3b41a815f1b689c
            82050c4f1a95faeb4fd34eada50028f855527ffeda4277a7563a050e81f5cd02
            f8d8497b096f759797cb51c47adef958a6245e6608126db1e840097e2b3afdf5
            ec3b0387ad3f84dec9d50646c6f06ecaff8fc14353c3ea314027c2877f5081bd
            94379be3651b81dbae45f5dccafa210dd8b265989fb5c4cd9702427b2570400d
            e6808d545b806da2e97a848c7d169a7062879482f8e165776156094e0823e552
            0c91d3f0593da9f292c97904f02a414b5d424c18ee6ff2d8fcbb53cdd465406d
            c9b81f689a5d315b27292d493cd049df1cd16e51d337fa3c89ec053bb253004a
            6143b0ad379b9b77f9dc3db4e6ffabb519a4d7345ce4accfc2befab721a5b1f0
            40b11635bc89f961327ae4d09ed80400a736d2a7fbb6b6e1b5fcb87cf5946c49
            b6ed63b25f787a788b97ea0204527b2edf1e25525acd8698ba14aba678f8f003
            46f1300fcb848de3bc688d2fe951c249af959b19d70d5a785a29562f2f80215e
            ccad1d8f42094a5878e5282bdde8ea2bd69dbc7b0edf586e8815c04b90b8095b
            5c8422a016947e87199596437e9b82617cc4094349a6792e7ef72d28018e02d7
            95403c7680aa9efb2fc26fa350e8e63fcf5aa594486d6af19266cd0cd097326a
            dcabdd7134ee0293bf0e48cdabfbb39ae560652d4c9119a33d608fdb8f07f1da
            7603936c9ff9a11da81a3684a2379e18f0281bb7a334b48ef91860e058c29289
            a05906dff1fa4844b9f54a7f048379011c2b93ca56e90434257a5c469debe5a6
            1edb890270688a337bdf6243dd1216a282210ab9a35b67cf91a4610b0df8cb85
            900c285972a9969b4d2d8bcd67dabccb817a2a77a102251d5dc1b2e254f095c8
            1b33a1b2bd404719ac3d6fb0de6d012507f913f971ce71e2b4969ab2191fde61
            aab85154a0311982161cfb43c5708ed5f69aee0bcb0916e95c41a97efb5465e0
            e37fd4c1397178271479b6fb59bcb30b623c89ce13ae0d0f8ad158118ed5b763
	    b84219798b644e97a473f99f9deef9e1985be1608fdbed794755dde80b694795
	    ae1b03ac0d10e6f5de8ac40670caf3204f2f38f2a3a3a3d29182a2fd5740edce
	    63082efb191f31c3bc4be28f7118aa38e53b0d18b4366cbdc275a628b36876ce
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
    extract_deb "${srcdir}"/i3xrocks-battery_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-cpu-usage_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-focused-window-name_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-key-indicator_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-media-player_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-memory_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-net-traffic_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-nm-vpn_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-openvpn_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-temp_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-time_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-volume_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-weather_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/i3xrocks-wifi_3.5.6-1_amd64.deb

#    patch "${pkgdir}"/usr/share/i3xrocks/net-traffic -i "${srcdir}"/net-traffic.patch
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
    extract_deb "${srcdir}"/regolith-look-ayu_2.6.14-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-ayu-dark_2.6.14-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-ayu-mirage_2.6.14-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-cahuella_2.6.14-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-dracula_2.6.14-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-gruvbox_2.6.14-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-lascaille_2.6.14-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-nord_2.6.14-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-pop-os_2.6.14-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-solarized-dark_2.6.14-1_amd64.deb
    extract_deb "${srcdir}"/regolith-look-ubuntu_2.6.14-1_amd64.deb
    extract_deb "${srcdir}"/regolith-styles_2.6.14-1_amd64.deb
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
    extract_deb "${srcdir}"/regolith-desktop-complete_2.106-1groovy_amd64.deb
    extract_deb "${srcdir}"/regolith-ftue_1.0.11-1_amd64.deb
    extract_deb "${srcdir}"/regolith-lightdm-config_1.0.6-1_amd64.deb
    extract_deb "${srcdir}"/regolith-i3-gaps-config_2.8.4-1_amd64.deb
    extract_deb "${srcdir}"/regolith-rofi-config_1.3.1-1_amd64.deb
    extract_deb "${srcdir}"/regolith-system_1.4.0.4-1_amd64.deb
    extract_deb "${srcdir}"/ubiquity-slideshow-regolith_138.5-ubuntu1~regolith1_all.deb
    extract_deb "${srcdir}"/regolith-i3xrocks-config_3.5.6-1_amd64.deb
    extract_deb "${srcdir}"/regolith-rofication_1.3.1-1_amd64.deb    

    move_copyright
## extra commands
    mv "${pkgdir}"/usr/lib/python3 "${pkgdir}"/usr/lib/python3.8
    mv "${pkgdir}"/usr/lib/python3.8/dist-packages "${pkgdir}"/usr/lib/python3.8/site-packages
    rm "${pkgdir}"/usr/share/backgrounds/lucas-bellator-C0OD8OM-oM0-unsplash.jpg
    rm "${pkgdir}"/usr/share/applications/reboot.desktop
    rm "${pkgdir}"/usr/share/applications/logout.desktop
    rm "${pkgdir}"/usr/share/applications/shutdown.desktop
    sed -i 's/x-terminal-emulator/st/g' "${pkgdir}"/etc/regolith/i3/config
}


package_regolith-st () {
	pkgdesc="Regolith's fork of st - the simple terminal"
	license=("MIT")
	provides=('st')
	conflicts=('st')

	extract_deb "${srcdir}"/regolith-st_0.8.2-1ubuntu20ppa5_amd64.deb

}
