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
pkgver=0.1.0
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
	"${url2}"/nordic_1.6.5-1ubuntu1ppa1_all.deb
	"${url2}"/plymouth-theme-regolith_1.0.3-1_all.deb
	"${url2}"/regolith-compositor-picom-glx_1.1.1-1_amd64.deb
	"${url2}"/regolith-default-settings_1.0.2-1groovy_amd64.deb
	"${url2}"/regolith-desktop-complete_2.92-1groovy_amd64.deb
	"${url2}"/regolith-ftue_1.0.11-1_amd64.deb
	"${url2}"/regolith-gdm3-theme_2.0.0-1ubuntu1~ppa1_amd64.deb
	"${url2}"/regolith-gnome-flashback_2.6.2-1_amd64.deb
	"${url2}"/regolith-i3-gaps-config_2.8.0-1_amd64.deb
	"${url2}"/regolith-lightdm-config_1.0.6-1_amd64.deb
	"${url2}"/regolith-look-ayu_2.6.13-1ubuntu2_amd64.deb
	"${url2}"/regolith-look-ayu-dark_2.6.13-1ubuntu2_amd64.deb
	"${url2}"/regolith-look-ayu-mirage_2.6.13-1ubuntu2_amd64.deb
	"${url2}"/regolith-look-cahuella_2.6.13-1ubuntu2_amd64.deb
	"${url2}"/regolith-look-lascaille_2.6.13-1ubuntu2_amd64.deb
	"${url2}"/regolith-look-nord_2.6.13-1ubuntu2_amd64.deb
	"${url2}"/regolith-look-solarized-dark_2.6.13-1ubuntu2_amd64.deb
	"${url2}"/regolith-look-ubuntu_2.6.13-1ubuntu2_amd64.deb
        "${url2}"/regolith-look-pop-os_2.6.13-1ubuntu2_amd64.deb
	"${url2}"/regolith-rofication_1.2.3-1_amd64.deb
	"${url2}"/regolith-rofi-config_1.3.1-1_amd64.deb
	"${url5}"/regolith-st_0.8.2-1ubuntu20ppa5_amd64.deb
	"${url2}"/regolith-styles_2.6.13-1ubuntu2_amd64.deb
	"${url2}"/regolith-system_1.4.0.4-1_amd64.deb
	"${url2}"/solarc-theme_800c997-1_amd64.deb
	"${url5}"/ubiquity-slideshow-regolith_138.5-ubuntu1~regolith1_all.deb
	"${url5}"/xrescat_1.1-1ubuntu1ppa1_amd64.deb
	"${url5}"/i3xrocks-battery_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-cpu-usage_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-focused-window-name_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-key-indicator_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-media-player_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-memory_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-net-traffic_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-nm-vpn_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-openvpn_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-temp_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-time_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-volume_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-weather_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-wifi_3.2.6-1ubuntu2_amd64.deb
	"${url5}"/i3xrocks-info_3.2.6-1ubuntu2_amd64.deb
	"${url2}"/regolith-i3xrocks-config_3.2.6-1ubuntu2_amd64.deb
        flashback.patch)
        #flashback2.patch)

#sha256sums=('cf0d111e9bc12e163b930849105626e535550d066bac280052d83a0e4d458818'
#            '22bbf4aaf1870963befffae41bfe7c2a0c8b674b4b0d15554a68b80a5f2429e3'
#            '2c4060dda3ee2d3b4fc587d35a8e9c9e6e8e7cc63edf72cf1e17322b1700d902'
#            '9fda771a69323114150a5ac95f588fe94934e5106d950037056507fc9bfc24c0'    # i3xrocks
#            '05c66c372d378d2992ec59be553bd7de1cf0574d61313d84274f1e64bfe23d3b'
#            'f9fabeb0442eb849a8e95163c20fbf9b40f288af0812583b270120e4d8092608'    # plymouth-theme-regolith
#            'c17619b9405a0fbf8a6626bf0cfde7631bee457f9d9af82b2099d3833a71f35c'    # regolith-compositor-compton-glx
#            '2722c4fdac1e120d2dda9e309ac85fed583e6eb738efe3cf3cbf389288aa5138'
#            '09201968ab0bcc63a46110e006680f1cbd807fdd4fce16d4b4eba34115bac941'
#            '8f2c3d7168440644b1e426e61948dda758a9a7f7040c1dd3ee7d41b306f624dd'
#            '82050c4f1a95faeb4fd34eada50028f855527ffeda4277a7563a050e81f5cd02'
#            'a5dfec5bf96a24778364c03b1143fe20f835bafb269ec0efe59841bc461f0f7c'
#            'f279ba8d320f2197d9692e53142f60355f519afdb3d724ccbe8d720615de4618'    # regolith-i3-gaps-config
#            'e6808d545b806da2e97a848c7d169a7062879482f8e165776156094e0823e552'
#            '34323f51e63cac850262dc2d1ae44583c6678c1303e0faf4b5eb341cb953c1f2'
#            'f10f62cb431b1b8f70c706052a556dc2ff9801ecc0df0fadac292229ef87378e'
#            '5f1ad1df62a1a15f95e744d7a8eb2d0852ad00500050a7185dc98792ecd0b90f'
#            '78866fb8c7ad2d3079ed350eaa679b92bc96c6d8a5707bdc9c80f3ca91e4d6f2'
#            '7fa0bec204ebafae295ac873458a8bd0dabc273c9d99036a89f937a614a671ca'
#            '9e9825270ed40386e8b170834b9d331a6dab55624a7996cb56f3e9b664f32538'
#            '2d3707829ba24f60af0d7310b0f95a79ec6eb28f7eb3224b3a7419b35dc70858'
#            'ab7f7e25566327afc15baa23990ae0d5522132645a9f6331504f1d01eeff174e'
#            '636366aad3a4635e3df5ecc69bafa2f176d7f2c09fa9a472825dbb508119bf96'
#            '7e390253850eb2f7fd3bcf1638c5e2c005a524be58a743d57ce14194f0eb78ee'    # regolith-rofi-config
#            '900c285972a9969b4d2d8bcd67dabccb817a2a77a102251d5dc1b2e254f095c8'
#            '4b5479da8f81650965660f01470703cc52110d7b29b68d6b6db8d1427a7a4cc7'    # regolith-styles
#            'be2d3143a741b183f69f97fc719034e24e5f77d7e210b890db1ddf416335c267'    # 
#            'e37fd4c1397178271479b6fb59bcb30b623c89ce13ae0d0f8ad158118ed5b763'    # 
#            'b84219798b644e97a473f99f9deef9e1985be1608fdbed794755dde80b694795'    # 
#            '9c641ad29504864ed08cd67f34583e72f67143a784ee058f37ec703e0b823ad0'    # xrescat
#            'e889377bb341c84d8f695e88cf315621f3bad68f33aebb637c6e3fad88bc0fb2'    # i3xrocks-battery
#            '4d41500a2ed6f24b188b814138b8a3fff663c29f1fb9ed24607affdb2d8acddd'    # i3xrocks-cpu-usage
#            'b3226129555a1c445c90765c9929b6f32e14e45094551e231d3ab5430618996e'    # i3xrocks-focused-window-name
#            '62356ea32008c94de74047515afc4d623bb6bc6c9f186402160ea9c528ec46e5'    # i3xrocks-key-indicator
#            '77e98869776f6628d3b04aaba78b8eb9ca507ec8082ae6979686f78cee9e26b1'    # i3xrocks-media-player
#            '41d2dfe6063f8488b7b695fa377ca82e2b4c78e1d4203bf29a5e9382d3be523f'    # i3xrocks-memory
#            '46cac7cfa1bf953232d578447f65d3be8fe5582935daec77ccdfe1b7abce13f8'    # i3xrocks-net-traffic
#            '3d1affdda45aff0ee1ba163c640c2861ed214fa93f608b2fea5981dc4eac96dc'    # i3xrocks-nm-vpn
#            'f51450f23b53cadb5805c44f66cf30354d290b42289a4a49a0522d1d607c1401'    # i3xrocks-openvpn
#            'bdbfa199c54f4a664967dee06adb58b31540ec24d4490904c85354cac35f5591'    # i3xrocks-temp
#            '94a30ba50bb52637671b7eb05a20f47dccdb687fc94a66e7d5c92d2816c7aaa2'    # i3xrocks-time
#            '065b0dbc19d2dc5539c5a1e5296982a5833d155af78d97289c2f26c584c2cafb'    # i3xrocks-volume
#            'e4435949ba1410cc3b1a165584da425d1a549a16b4e048bc6c645fa31f845729'    # i3xrocks-weather
#            'ded21170d8e0fa88bb421139188cd97edc24f2ff2d74df35af077c43375c074e'    # i3xrocks-wifi
#            '74b54a5415a4bdd2aa08ed239f2a69e28be3e9808c174df4dcc60031ccad1a4c'    # i3xrocks-info
#            '40bc5ac9894fd087c814de21ca02c16f506c55351f16d98baee66cdcd608a5be'    # regolith-i3xrocks-config
#            'fa7b230613d9c286ee549a57cc528701f8d0869846cc98bb580b60c435fa563a'    # flashback.patch
#            'fb8d508bbfcb0adc70c7a8d16f649eb03d3dfce505ef9289db1ad939605a9649')   # flashback2.patch

sha256sums=('SKIP'
	    'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
	    'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
#            'SKIP'
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
    provides=('i3-snapshot')
    conflicts=()

    extract_deb "${srcdir}"/i3-snapshot_1.0-1ubuntu1~ppa1_amd64.deb
    extract_deb "${srcdir}"/regolith-gnome-flashback_2.6.2-1_amd64.deb
    extract_deb "${srcdir}"/xrescat_1.1-1ubuntu1ppa1_amd64.deb
    
    # extra command
    patch "${pkgdir}"/usr/bin/regolith-session -i "${srcdir}"/flashback.patch
#    patch "${pkgdir}"/usr/bin/i3-gnome-flashback -i "${srcdir}"/flashback2.patch

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

}


package_regolith-st () {
	pkgdesc="Regolith's fork of st - the simple terminal"
	license=("MIT")
	provides=('st')
	conflicts=('st')

	extract_deb "${srcdir}"/regolith-st_0.8.2-1ubuntu20ppa5_amd64.deb

}
