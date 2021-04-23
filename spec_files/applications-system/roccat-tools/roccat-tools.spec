Name: roccat
Version: 5.9.0
Release: 2
License: GPL
Source: https://sourceforge.net/projects/roccat/files/roccat-tools/roccat-tools-%{version}.tar.bz2
Patch0: fix-multiple-definitions.patch
BuildRequires: gtk2-devel >= 2.20
BuildRequires: cmake >= 2.6.4
BuildRequires: dbus-glib
BuildRequires: dbus-glib-devel
BuildRequires: libgudev1-devel
BuildRequires: libX11-devel
# BuildRequires: pkgconfig(dbus-glib) >= 0.110
# BuildRequires: pkgconfig(libgudev1) >= 234
# BuildRequires: pkgconfig(libX11) >= 1.6.12
BuildRequires: libgaminggear-devel >= 0.15.1
BuildRequires: pkgconfig(lua) >= %{luaversion}
BuildRequires: gettext >= 0.15
ExclusiveOS: linux
URL: http://roccat.sourceforge.net

%global debug_package %{nil}
%global _default_patch_fuzz 2

%define default_udevdir /lib/udev/rules.d
%{!?udevdir: %define udevdir %{default_udevdir}}

%define default_eventhandlerdir %{_libdir}/roccat
%{!?eventhandlerdir: %define eventhandlerdir %{default_eventhandlerdir}}

%define default_gfx_plugindir %{_libdir}/gaminggear_plugins
%{!?gfx_plugindir: %define gfx_plugindir %{default_gfx_plugindir}}

%define default_luaversion 5.4
%{!?luaversion: %define luaversion %{default_luaversion}}

Summary: Roccat common files

%package arvo
Requires: roccat
Summary: Roccat Arvo userlandtools
Group: Applications/System

%package isku
Requires: roccat
Summary: Roccat Isku userlandtools
Group: Applications/System

%package iskufx
Requires: roccat
Requires: roccat-isku
Summary: Roccat IskuFX userlandtools
Group: Applications/System

%package kiro
Requires: roccat
Summary: Roccat Kiro userlandtools
Group: Applications/System

%package kone
Requires: roccat
Summary: Roccat Kone userlandtools
Group: Applications/System

%package koneplus
Requires: roccat
Summary: Roccat Kone[+] userlandtools
Group: Applications/System

%package konepure
Requires: roccat
Requires: roccat-konextd
Summary: Roccat KonePure userlandtools
Group: Applications/System

%package konepuremilitary
Requires: roccat
Requires: roccat-konepure
Summary: Roccat KonePureMilitary/Black userlandtools
Group: Applications/System

%package konepureoptical
Requires: roccat
Requires: roccat-konepure
Summary: Roccat KonePureOptical userlandtools
Group: Applications/System

%package konextd
Requires: roccat
Requires: roccat-koneplus
Summary: Roccat KoneXTD userlandtools
Group: Applications/System

%package konextdoptical
Requires: roccat
Requires: roccat-konepuremilitary
Summary: Roccat KoneXTDOptical userlandtools
Group: Applications/System

%package kova2016
Requires: roccat
Summary: Roccat Kova 2016 userlandtools
Group: Applications/System

%package kovaplus
Requires: roccat
Summary: Roccat Kova[+] userlandtools
Group: Applications/System

%package lua
Requires: roccat
Summary: Roccat Lua userlandtools
Group: Applications/System

%package nyth
Requires: roccat
Summary: Roccat Nyth userlandtools
Group: Applications/System

%package pyra
Requires: roccat
Summary: Roccat Pyra userlandtools
Group: Applications/System

%package ryosmk
Requires: roccat
Requires: lua >= %{luaversion}
Obsoletes: roccat-ryos
Summary: Roccat Ryos MK userlandtools
Group: Applications/System

%package ryosmkfx
Requires: roccat
Requires: roccat-ryosmk
Requires: lua >= %{luaversion}
Summary: Roccat Ryos MK FX userlandtools
Group: Applications/System

%package ryostkl
Requires: roccat
Requires: roccat-ryosmk
Requires: lua >= %{luaversion}
Summary: Roccat Ryos TKL userlandtools
Group: Applications/System

%package savu
Requires: roccat
Summary: Roccat Savu userlandtools
Group: Applications/System

%package skeltr
Requires: roccat
Summary: Roccat Skeltr userlandtools
Group: Applications/System

%package sova
Requires: roccat
Summary: Roccat Sova userlandtools
Group: Applications/System

%package suora
Requires: roccat
Summary: Roccat Suora userlandtools
Group: Applications/System

%package tyon
Requires: roccat
Summary: Roccat Tyon userlandtools
Group: Applications/System

%description
Roccat consists of a shared library and other files shared by device specific
applications for roccat hardware.

%description arvo
Arvo consists of a console application and a GUI application. It helps users to
manipulate the Profiles and Settings of a Roccat Arvo keyboard.

%description isku
Isku consists of a console application and a GUI application. It helps users to
manipulate the Profiles and Settings of a Roccat Isku keyboard.

%description iskufx
IskuFX consists of a console application and a GUI application. It helps users to
manipulate the Profiles and Settings of a Roccat IskuFX keyboard.

%description kiro
Kiro consists of a console application and a GUI application. It helps users
to manipulate the Profiles and Settings of a Roccat Kiro mouse.

%description kone
Kone consists of a console application and a GUI application. It helps users to
manipulate the Profiles and Settings of a Roccat Kone mouse.

%description koneplus
Koneplus consists of a console application and a GUI application. It helps users
to manipulate the Profiles and Settings of a Roccat Kone[+] mouse.

%description konepure
Konepure consists of a console application and a GUI application. It helps users
to manipulate the Profiles and Settings of a Roccat KonePure mouse.

%description konepuremilitary
Konepuremilitary consists of a console application and a GUI application. It helps
to manipulate the Profiles and Settings of a Roccat KonePureMilitary/Black mouse.

%description konepureoptical
Konepureoptical consists of a console application and a GUI application. It helps
users to manipulate the Profiles and Settings of a Roccat KonePureOptical mouse.

%description konextd
Konextd consists of a console application and a GUI application. It helps users
to manipulate the Profiles and Settings of a Roccat KoneXTD mouse.

%description konextdoptical
Konextdoptical consists of a console application and a GUI application. It helps
users to manipulate the Profiles and Settings of a Roccat KoneXTDOptical mouse.

%description kova2016
Kova2016 consists of a console application and a GUI application. It helps users
to manipulate the Profiles and Settings of a Roccat Kova 2016 mouse.

%description kovaplus
Kovaplus consists of a console application and a GUI application. It helps users
to manipulate the Profiles and Settings of a Roccat Kova[+] mouse.

%description lua
Lua consists of a console application and a GUI application. It helps users to
manipulate the Settings of a Roccat Lua mouse.

%description nyth
Nyth consists of a console application and a GUI application. It helps users to
manipulate the Settings of a Roccat Nyth mouse.

%description pyra
Pyra consists of a console application and a GUI application. It helps users to
manipulate the Profiles and Settings of a Roccat Pyra mouse.

%description ryosmk
Ryosmk consists of a console application and a GUI application. It helps users
to manipulate the Profiles and Settings of Roccat Ryos MK keyboards.

%description ryostkl
Ryostkl consists of a console application and a GUI application. It helps users
to manipulate the Profiles and Settings of Roccat Ryos TKL keyboards.

%description ryosmkfx
Ryosmkfx consists of a console application and a GUI application. It helps users
to manipulate the Profiles and Settings of Roccat Ryos MK FX keyboards.

%description savu
Savu consists of a console application and a GUI application. It helps users to
manipulate the Profiles and Settings of a Roccat Savu mouse.

%description skeltr
Skeltr consists of a console application and a GUI application. It helps users to
manipulate the Profiles and Settings of a Roccat Skeltr keyboard.

%description sova
Sova consists of a console application and a GUI application. It helps users to
manipulate the Profiles and Settings of a Roccat Sova keyboard.

%description suora
Suora consists of a console application and a GUI application. It helps users to
manipulate the Profiles and Settings of a Roccat Suora keyboard.

%description tyon
Tyon consists of a console application and a GUI application. It helps users to
manipulate the Profiles and Settings of a Roccat Tyon mouse.

%prep
%setup -q -n roccat-tools-%{version}
%patch0 -p1
%{__mkdir} build
cd build
CFLAGS="-isystem /usr/include/harfbuzz" cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="%{_prefix}" -DLIBDIR="%{_libdir}" -DUDEVDIR="%{udevdir}" -DEVENTHANDLER_PLUGIN_DIR="%{eventhandlerdir}" -DWITH_LUA="5.4" -DWITH_LUA=%{luaversion} ..

%build
cd build
%{__make} %{?_smp_mflags}

%install
cd build
%{__make} %{?_smp_mflags} DESTDIR="%{buildroot}" install
%{__mkdir} -p "%{buildroot}/var/lib/roccat"

%pre
/usr/sbin/groupadd --force --system roccat >/dev/null || :

%post
/sbin/ldconfig
touch --no-create %{_prefix}/share/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
  touch --no-create %{_prefix}/share/icons/hicolor &>/dev/null
  gtk-update-icon-cache %{_prefix}/share/icons/hicolor &>dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_prefix}/share/icons/hicolor &>dev/null || :

%post arvo
/sbin/ldconfig

%postun arvo
/sbin/ldconfig

%post isku
/sbin/ldconfig

%postun isku
/sbin/ldconfig

%post iskufx
/sbin/ldconfig

%postun iskufx
/sbin/ldconfig

%post kiro
/sbin/ldconfig

%postun kiro
/sbin/ldconfig

%post kone
/sbin/ldconfig

%postun kone
/sbin/ldconfig

%post koneplus
/sbin/ldconfig

%postun koneplus
/sbin/ldconfig

%post konepure
/sbin/ldconfig

%postun konepure
/sbin/ldconfig

%post konepuremilitary
/sbin/ldconfig

%postun konepuremilitary
/sbin/ldconfig

%post konepureoptical
/sbin/ldconfig

%postun konepureoptical
/sbin/ldconfig

%post konextd
/sbin/ldconfig

%post konextdoptical
/sbin/ldconfig

%postun konextd
/sbin/ldconfig

%post kova2016
/sbin/ldconfig

%postun kova2016
/sbin/ldconfig

%post kovaplus
/sbin/ldconfig

%postun kovaplus
/sbin/ldconfig

%post lua
/sbin/ldconfig

%postun lua
/sbin/ldconfig

%post nyth
/sbin/ldconfig

%postun nyth
/sbin/ldconfig

%post pyra
/sbin/ldconfig

%postun pyra
/sbin/ldconfig

%post ryosmk
/sbin/ldconfig

%postun ryosmk
/sbin/ldconfig

%post ryosmkfx
/sbin/ldconfig

%postun ryosmkfx
/sbin/ldconfig

%postun ryostkl
/sbin/ldconfig

%post savu
/sbin/ldconfig

%postun savu
/sbin/ldconfig

%post skeltr
/sbin/ldconfig

%postun skeltr
/sbin/ldconfig

%post sova
/sbin/ldconfig

%postun sova
/sbin/ldconfig

%post suora
/sbin/ldconfig

%postun suora
/sbin/ldconfig

%post tyon
/sbin/ldconfig

%postun tyon
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc README COPYING Changelog
%{_bindir}/roccateventhandler
%{_libdir}/libroccat.so*
%{_libdir}/libroccatwidget.so*
%{_datadir}/icons
%{_datadir}/roccat/sounds
/etc/xdg/autostart/roccateventhandler.desktop
%{_datadir}/locale/*/LC_MESSAGES/roccat-tools.mo
%attr(2770,root,roccat) /var/lib/roccat

%files arvo
%defattr(-,root,root)
%{udevdir}/90-roccat-arvo.rules
%{_bindir}/roccatarvo*
%{_libdir}/libroccatarvo.so*
%{eventhandlerdir}/libarvoeventhandler.so
%{_datadir}/applications/roccatarvoconfig.desktop
%{_mandir}/*/man1/roccatarvo*

%files isku
%defattr(-,root,root)
%{udevdir}/90-roccat-isku.rules
%{_bindir}/roccatisku*
%{_libdir}/libroccatisku.so*
%{_libdir}/libroccatiskuwidget.so*
%{eventhandlerdir}/libiskueventhandler.so
%{_datadir}/applications/roccatiskuconfig.desktop
%{_mandir}/*/man1/roccatisku*

%files iskufx
%defattr(-,root,root)
%{udevdir}/90-roccat-iskufx.rules
%{_bindir}/roccatiskufx*
%{_libdir}/libroccatiskufx.so*
%{eventhandlerdir}/libiskufxeventhandler.so
%{gfx_plugindir}/libiskufxgfxplugin.so
%{_datadir}/applications/roccatiskufxconfig.desktop
%{_mandir}/*/man1/roccatiskufx*

%files kiro
%defattr(-,root,root)
%{udevdir}/90-roccat-kiro.rules
%{_bindir}/roccatkiro*
%{_libdir}/libroccatkiro.so*
%{eventhandlerdir}/libkiroeventhandler.so
%{gfx_plugindir}/libkirogfxplugin.so
%{_datadir}/applications/roccatkiroconfig.desktop
%{_mandir}/*/man1/roccatkiro*

%files kone
%defattr(-,root,root)
%{udevdir}/90-roccat-kone.rules
%{_bindir}/roccatkone*
%{_libdir}/libroccatkone.so*
%{eventhandlerdir}/libkoneeventhandler.so
%{_datadir}/applications/roccatkoneconfig.desktop
%{_mandir}/*/man1/roccatkone*

%files koneplus
%defattr(-,root,root)
%{udevdir}/90-roccat-koneplus.rules
%{_bindir}/roccatkoneplus*
%{_libdir}/libroccatkoneplus.so*
%{_libdir}/libroccatkonepluswidget.so*
%{eventhandlerdir}/libkonepluseventhandler.so
%{gfx_plugindir}/libkoneplusgfxplugin.so
%{_datadir}/applications/roccatkoneplusconfig.desktop
%{_mandir}/*/man1/roccatkoneplus*

%files konepure
%defattr(-,root,root)
%{udevdir}/90-roccat-konepure.rules
%{_bindir}/roccatkonepure*
%{_libdir}/libroccatkonepure.so*
%{_libdir}/libroccatkonepurewidget.so*
%{eventhandlerdir}/libkonepureeventhandler.so
%{gfx_plugindir}/libkonepuregfxplugin.so
%{_datadir}/applications/roccatkonepureconfig.desktop
%{_mandir}/*/man1/roccatkonepure*

%files konepuremilitary
%defattr(-,root,root)
%{udevdir}/90-roccat-konepuremilitary.rules
%{_bindir}/roccatkonepuremilitary*
%{_libdir}/libroccatkonepuremilitary.so*
%{_libdir}/libroccatkonepuremilitarywidget.so*
%{eventhandlerdir}/libkonepuremilitaryeventhandler.so
%{gfx_plugindir}/libkonepuremilitarygfxplugin.so
%{_datadir}/applications/roccatkonepuremilitaryconfig.desktop
%{_mandir}/*/man1/roccatkonepuremilitary*

%files konepureoptical
%defattr(-,root,root)
%{udevdir}/90-roccat-konepureoptical.rules
%{_bindir}/roccatkonepureoptical*
%{_libdir}/libroccatkonepureoptical.so*
%{eventhandlerdir}/libkonepureopticaleventhandler.so
%{gfx_plugindir}/libkonepureopticalgfxplugin.so
%{_datadir}/applications/roccatkonepureopticalconfig.desktop
%{_mandir}/*/man1/roccatkonepureoptical*

%files konextd
%defattr(-,root,root)
%{udevdir}/90-roccat-konextd.rules
%{_bindir}/roccatkonextd*
%{_libdir}/libroccatkonextd.so*
%{_libdir}/libroccatkonextdwidget.so*
%{eventhandlerdir}/libkonextdeventhandler.so
%{gfx_plugindir}/libkonextdgfxplugin.so
%{_datadir}/applications/roccatkonextdconfig.desktop
%{_mandir}/*/man1/roccatkonextd*

%files konextdoptical
%defattr(-,root,root)
%{udevdir}/90-roccat-konextdoptical.rules
%{_bindir}/roccatkonextdoptical*
%{_libdir}/libroccatkonextdoptical.so*
%{eventhandlerdir}/libkonextdopticaleventhandler.so
%{gfx_plugindir}/libkonextdopticalgfxplugin.so
%{_datadir}/applications/roccatkonextdopticalconfig.desktop
%{_mandir}/*/man1/roccatkonextdoptical*

%files kova2016
%defattr(-,root,root)
%{udevdir}/90-roccat-kova2016.rules
%{_bindir}/roccatkova2016*
%{_libdir}/libroccatkova2016.so*
%{eventhandlerdir}/libkova2016eventhandler.so
%{gfx_plugindir}/libkova2016gfxplugin.so
%{_datadir}/applications/roccatkova2016config.desktop
%{_mandir}/*/man1/roccatkova2016*

%files kovaplus
%defattr(-,root,root)
%{udevdir}/90-roccat-kovaplus.rules
%{_bindir}/roccatkovaplus*
%{_libdir}/libroccatkovaplus.so*
%{eventhandlerdir}/libkovapluseventhandler.so
%{_datadir}/applications/roccatkovaplusconfig.desktop
%{_mandir}/*/man1/roccatkovaplus*

%files lua
%defattr(-,root,root)
%{udevdir}/90-roccat-lua.rules
%{_bindir}/roccatlua*
%{_libdir}/libroccatlua.so*
%{eventhandlerdir}/libluaeventhandler.so
%{_datadir}/applications/roccatluaconfig.desktop
%{_mandir}/*/man1/roccatlua*

%files nyth
%defattr(-,root,root)
%{udevdir}/90-roccat-nyth.rules
%{_bindir}/roccatnyth*
%{_libdir}/libroccatnyth.so*
%{eventhandlerdir}/libnytheventhandler.so
%{gfx_plugindir}/libnythgfxplugin.so
%{_datadir}/applications/roccatnythconfig.desktop
%{_mandir}/*/man1/roccatnyth*

%files pyra
%defattr(-,root,root)
%{udevdir}/90-roccat-pyra.rules
%{_bindir}/roccatpyra*
%{_libdir}/libroccatpyra.so*
%{eventhandlerdir}/libpyraeventhandler.so
%{_datadir}/applications/roccatpyraconfig.desktop
%{_mandir}/*/man1/roccatpyra*

%files ryosmk
%defattr(-,root,root)
%{udevdir}/90-roccat-ryosmk.rules
%{_bindir}/roccatryosmk*
%{_libdir}/libroccatryosmk.so*
%{_libdir}/libroccatryosmkwidget.so*
%{eventhandlerdir}/libryosmkeventhandler.so
%{_datadir}/applications/roccatryosmkconfig.desktop
%{_mandir}/*/man1/roccatryosmk*
%{_datadir}/roccat/ryos_effect_modules

%files ryosmkfx
%defattr(-,root,root)
%{udevdir}/90-roccat-ryosmkfx.rules
%{_bindir}/roccatryosmkfx*
%{_libdir}/libroccatryosmkfx.so*
%{eventhandlerdir}/libryosmkfxeventhandler.so
%{gfx_plugindir}/libryosmkfxgfxplugin.so
%{_datadir}/applications/roccatryosmkfxconfig.desktop
%{_mandir}/*/man1/roccatryosmkfx*

%files ryostkl
%defattr(-,root,root)
%{udevdir}/90-roccat-ryostkl.rules
%{_bindir}/roccatryostkl*
%{_libdir}/libroccatryostkl.so*
%{eventhandlerdir}/libryostkleventhandler.so
%{_datadir}/applications/roccatryostklconfig.desktop
%{_mandir}/*/man1/roccatryostkl*

%files savu
%defattr(-,root,root)
%{udevdir}/90-roccat-savu.rules
%{_bindir}/roccatsavu*
%{_libdir}/libroccatsavu.so*
%{eventhandlerdir}/libsavueventhandler.so
%{_datadir}/applications/roccatsavuconfig.desktop
%{_mandir}/*/man1/roccatsavu*

%files skeltr
%defattr(-,root,root)
%{udevdir}/90-roccat-skeltr.rules
%{_bindir}/roccatskeltr*
%{_libdir}/libroccatskeltr.so*
%{eventhandlerdir}/libskeltreventhandler.so
%{gfx_plugindir}/libskeltrgfxplugin.so
%{_datadir}/applications/roccatskeltrconfig.desktop
%{_mandir}/*/man1/roccatskeltr*

%files sova
%defattr(-,root,root)
%{udevdir}/90-roccat-sova.rules
%{_bindir}/roccatsova*
%{_libdir}/libroccatsova.so*
%{eventhandlerdir}/libsovaeventhandler.so
%{_datadir}/applications/roccatsovaconfig.desktop
%{_mandir}/*/man1/roccatsova*

%files suora
%defattr(-,root,root)
%{udevdir}/90-roccat-suora.rules
%{_bindir}/roccatsuora*
%{_libdir}/libroccatsuora.so*
%{eventhandlerdir}/libsuoraeventhandler.so
%{_datadir}/applications/roccatsuoraconfig.desktop
%{_mandir}/*/man1/roccatsuora*

%files tyon
%defattr(-,root,root)
%{udevdir}/90-roccat-tyon.rules
%{_bindir}/roccattyon*
%{_libdir}/libroccattyon.so*
%{eventhandlerdir}/libtyoneventhandler.so
%{gfx_plugindir}/libtyongfxplugin.so
%{_datadir}/applications/roccattyonconfig.desktop
%{_mandir}/*/man1/roccattyon*

%changelog
* Fri Apr 23 2021 Kevin Faulkner <kondor6c@lazytree.us> 5.7.0-2
- altered spec file for Fedora 33, new Lua version, pangolibs
- patch from Stefan ryos build issue https://aur.archlinux.org/pkgbase/roccat-tools/#comment-753814
* Tue Jun 13 2017 Stefan Achatz <erazor_de@users.sourceforge.net> 5.7.0-1
- Initial version
