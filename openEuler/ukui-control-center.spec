%define debug_package %{nil}
Name:           ukui-control-center
Version:        3.0.1
Release:        5
Summary:        utilities to configure the UKUI desktop
License:        GPL-2+
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: gsettings-qt-devel
BuildRequires: glib2-devel
BuildRequires: libmatekbd-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: libxklavier-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: libkscreen-qt5-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: dconf-devel
BuildRequires: edid-decode
BuildRequires: redshift
BuildRequires: libmatemixer-devel
BuildRequires: libqtxdg-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: libxml2-devel
BuildRequires: libcanberra-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: mate-desktop-devel
BuildRequires: libX11-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbfile-devel
BuildRequires: boost-devel
BuildRequires: libxcb-devel
BuildRequires: qt5-linguist
BuildRequires: polkit-qt5-1-devel
BuildRequires: kf5-bluez-qt-devel
BuildRequires: pulseaudio-devel

Requires: dconf
Requires: qt5-qtimageformats
Requires: qt5-qtsvg-devel
Requires: gsettings-qt-devel
Requires: glib2-devel
Requires: libmatekbd-devel
Requires: qt5-qtx11extras-devel
Requires: libxklavier-devel
Requires: kf5-kwindowsystem-devel
Requires: kf5-kwidgetsaddons-devel
Requires: kf5-kconfig-devel
Requires: kf5-kconfigwidgets-devel
Requires: kf5-ki18n-devel
Requires: libkscreen-qt5-devel
Requires: qt5-qtdeclarative-devel
Requires: dconf-devel
Requires: edid-decode
Requires: redshift
Requires: libmatemixer-devel
Requires: libqtxdg-devel
Requires: qt5-qtmultimedia-devel
Requires: libxml2-devel
Requires: network-manager-applet
Requires: libcanberra-devel
Requires: qt5-qtgraphicaleffects
Requires: qt5-qtquickcontrols

Recommends: qt5-qtquickcontrols

Suggests: gsettings-desktop-schemas
Suggests: mate-common
Suggests: ukui-power-manager
Suggests: ukui-session-manager
Suggests: ukui-screensaver
Suggests: ukui-settings-daemon


%description
 The UKUI control center contains configuration applets for the UKUI desktop,
 allowing to set accessibility configuration, desktop fonts, keyboard
 and mouse properties, sound setup, desktop theme and background, user
 interface properties, screen resolution, and other UKUI parameters.

%prep
%setup -q

%build
qmake-qt5
make

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

%post
set -e
glib-compile-schemas /usr/share/glib-2.0/schemas/

#systemctl enable ukui-group-manager.service
#systemctl start  ukui-group-manager.service
chown root:root /usr/bin/checkuserpwd
chmod u+s /usr/bin/checkuserpwd

%preun
#systemctl disable ukui-group-manager.service
#systemctl stop ukui-group-manager.service

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/dbus-1/system.d/com.control.center.qt.systemdbus.conf
%{_sysconfdir}/dbus-1/system.d/org.ukui.groupmanager.conf
%{_bindir}/checkuserpwd
%{_bindir}/group-manager-server
%{_bindir}/launchSysDbus
%{_bindir}/ukui-control-center
%{_bindir}/ukui-control-center-session
%{_unitdir}/ukui-group-manager.service
%{_libdir}/ukui-control-center/libabout.so
%{_libdir}/ukui-control-center/libarea.so
%{_libdir}/ukui-control-center/libaudio.so
%{_libdir}/ukui-control-center/libautoboot.so
%{_libdir}/ukui-control-center/libbackup.so
%{_libdir}/ukui-control-center/libdatetime.so
%{_libdir}/ukui-control-center/libdefaultapp.so
%{_libdir}/ukui-control-center/libdesktop.so
%{_libdir}/ukui-control-center/libdisplay.so
%{_libdir}/ukui-control-center/libexperienceplan.so
%{_libdir}/ukui-control-center/libfonts.so
%{_libdir}/ukui-control-center/libkeyboard.so
%{_libdir}/ukui-control-center/libmouse.so
%{_libdir}/ukui-control-center/libnetconnect.so
%{_libdir}/ukui-control-center/libnetworkaccount.so
%{_libdir}/ukui-control-center/libnotice.so
%{_libdir}/ukui-control-center/libpower.so
%{_libdir}/ukui-control-center/libprinter.so
%{_libdir}/ukui-control-center/libproxy.so
%{_libdir}/ukui-control-center/libscreenlock.so
%{_libdir}/ukui-control-center/libscreensaver.so
%{_libdir}/ukui-control-center/libsecuritycenter.so
%{_libdir}/ukui-control-center/libshortcut.so
%{_libdir}/ukui-control-center/libtheme.so
%{_libdir}/ukui-control-center/libtouchpad.so
%{_libdir}/ukui-control-center/libupdate.so
%{_libdir}/ukui-control-center/libuserinfo.so
%{_libdir}/ukui-control-center/libvino.so
%{_libdir}/ukui-control-center/libvpn.so
%{_libdir}/ukui-control-center/libwallpaper.so
%{_datadir}/applications/ukui-control-center.desktop
%{_datadir}/dbus-1/services/org.ukui.ukcc.session.service
%{_datadir}/dbus-1/system-services/com.control.center.qt.systemdbus.service
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.desktop.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.experienceplan.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.keybinding.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.keyboard.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.notice.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.panel.plugins.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.personalise.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.wifi.switch.gschema.xml
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/about.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/account-add.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/account-edit.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/account-face.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/account-pwd.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/account-type.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/account.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/add-autoboot.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/add-shortcut.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/area-format.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/area.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/audio.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/autoboot.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/background.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/backup.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/blutooth.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/cloudaccount.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/datetime-change.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/datetime-zone.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/datetime.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/default.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/delegate.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/desktop.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/display.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/font.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/keyboard.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/mouse.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/netconnect.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/notice.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/power-custom.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/power.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/printer.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/screenlock.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/screensaver.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/security.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/shortcut.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/theme-cursor.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/theme-effect.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/theme.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/touchpad.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/ukcc.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/update.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/vino.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/image/vpn.png
%{_datadir}/kylin-user-guide/data/guide/ukui-control-center/zh_CN/index.md
%{_datadir}/locale/zh_CN/LC_MESSAGES/installer-timezones.mo
%{_datadir}/polkit-1/actions/org.ukui.groupmanager.policy
%{_datadir}/ukui-control-center/shell/res/i18n/bo.qm
%{_datadir}/ukui-control-center/shell/res/i18n/bo_CN.qm
%{_datadir}/ukui-control-center/shell/res/i18n/de.qm
%{_datadir}/ukui-control-center/shell/res/i18n/en_US.qm
%{_datadir}/ukui-control-center/shell/res/i18n/fa.qm
%{_datadir}/ukui-control-center/shell/res/i18n/fr.qm
%{_datadir}/ukui-control-center/shell/res/i18n/tr.qm
%{_datadir}/ukui-control-center/shell/res/i18n/zh_CN.qm
%{_datadir}/ukui/faces/1.png
%{_datadir}/ukui/faces/10.png
%{_datadir}/ukui/faces/2.png
%{_datadir}/ukui/faces/3.png
%{_datadir}/ukui/faces/4.png
%{_datadir}/ukui/faces/5.png
%{_datadir}/ukui/faces/6.png
%{_datadir}/ukui/faces/7.png
%{_datadir}/ukui/faces/8.png
%{_datadir}/ukui/faces/9.png
%{_datadir}/ukui/faces/default.png
%{_datadir}/ukui/faces/default.svg

%changelog
* Wed Jan 27 2021 lvhan <lvhan@kylinos.cn> - 3.0.1-5
- update to upstream version 3.0.0-1

* Thu Jan 21 2021 lvhan <lvhan@kylinos.cn> - 3.0.1-4
- fix-blueman-tray-and-groupadd-autologin

* Thu Dec 3 2020 lvhan <lvhan@kylinos.cn> - 3.0.1-3
- fix dialog pop twice after modifying resolution
- fix effects mode not available

* Mon Nov 30 2020 lvhan <lvhan@kylinos.cn> - 3.0.1-2
- fix autologin nopasswdlogin failed
- fix system overview failed

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 3.0.1-1
- update to upstream version 3.0.0-1+1031

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 2.0.3-1
- Init package for openEuler
