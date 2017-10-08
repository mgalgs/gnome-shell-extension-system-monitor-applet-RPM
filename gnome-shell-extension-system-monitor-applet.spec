%global uuid system-monitor@paradoxxx.zero.gmail.com
%global gitname gnome-shell-system-monitor-applet
%global short_name system-monitor

%global commit 61b0a60d74776455785ddb7a95851c2381961f6c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gnome-shell-extension-system-monitor-applet
Version:        0
Release:        0.1.20171005git%{shortcommit}%{?dist}
Summary:        A Gnome shell system monitor extension

# The entire source code is GPLv3+ except convenience.js, which is BSD
License:        GPLv3+ and BSD
URL:            https://github.com/paradoxxxzero/gnome-shell-system-monitor-applet
Source0:        https://github.com/paradoxxxzero/gnome-shell-system-monitor-applet/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch

Requires:       gnome-shell >= 3.12.0

BuildRequires:  gettext glib2

%description
Display system information in gnome shell status bar, such as memory usage,
CPU usage, and network rate...

%prep
%setup -qn %{gitname}-%{commit}

%build
# Build translations
pushd po
  # Since rpm-build package depends on sed, bash and findutils packages, 
  # we can use find, sed, xargs and bash commands in build process
  find ./*/ -type f \( -name "*.po" -o -name "*.pot" \) -print | sed 's/\(.*\)\(\.po.*\)/\1/g' | xargs -I {} bash -c 'if [ ! -f "{}.po" ] && [ -f "{}.pot" ] ; then mv "{}.pot" "{}.po" ; fi ; msgfmt -o "{}.mo" "{}.po"'
popd

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -D -m 0644 %{uuid}/{convenience.js,extension.js,metadata.json,prefs.js,stylesheet.css,compat.js} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
install -D -m 0644 %{uuid}/schemas/org.gnome.shell.extensions.system-monitor.gschema.xml \
  %{buildroot}%{_datadir}/glib-2.0/schemas/

# Translations.
pushd po
  find ./*/ -type f -name "*.mo" -printf "install -pD -m 0644 %h/%f %{buildroot}%{_datadir}/locale/%h/LC_MESSAGES/%f\n" | sed 's/\.\///g' | xargs -I {} bash -c '{}'
popd

%find_lang %{short_name}

%files -f %{short_name}.lang
%doc README.md
%license COPYING
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.system-monitor.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}

%changelog
* Sat Oct 07 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0-0.1.20171005git61b0a60
- Spec file cleanup

* Thu Oct 05 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20171005git61b0a60
- Updated to new upstream release
- Fixed battery module error and crash

* Sat Sep 30 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170930gitf24f167
- Updated to new upstream release
- Added support for Gnome 3.26
- Added GPU usage (NVidia)
- Updated translations

* Thu Sep 28 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170928git0a9f7a0
- Updated to new upstream release

* Thu Aug 17 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170817git746f33d
- Updated to new upstream release

* Mon May 01 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170501git59f443e
- Updated to new upstream release

* Tue Apr 11 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170411git0948ded
- Updated to new upstream release

* Thu Dec 22 2016 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20161222git3967cdd
- Updated to new upstream release

* Tue Apr 05 2016 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20160405git8b31f07
- Updated to new upstream release

* Wed Sep 30 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150930git81d1c08
- spec file cleanup
- Updated to new upstream release

* Wed Apr 15 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150415git44abf9a
- Updated to new upstream release

* Wed Feb 04 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150204gitd04c136
- Updated to new upstream release
- Added correct %%license tag to license files

* Wed Jan 28 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150129git6b9973e
- Updated to new upstream release

* Wed Jan 28 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150128gitccafeef
- Updated to new upstream release

* Fri Oct 10 2014 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.git59767af
- Updated to new upstream release

* Wed May 07 2014 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.git1b632f9
- Updated to new upstream release

* Wed Mar 06 2013 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - v24-0.1.gitfcecbaa
- Updated to new upstream release

* Sun Jan 13 2013 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - v24-0.1.git3f2c93e
- Updated to new upstream release

* Sun Oct 21 2012 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - v24-0.1.gitec4b4b7
- Updated to new upstream release v24

* Fri Aug 31 2012 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - v18-0.1.git96a05d5
- Updated to new upstream release v18

* Sun Aug 19 2012 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 2.0b1-0.1.git74500bd
- Updated to new upstream release 2.0b1
- Completed spec file to install translations

* Sun Jun 26 2011 Fabian Affolter <fabian@bernewireless.net> - 1.92-1
- Updated to new upstream release 1.92

* Sat Jun 18 2011 Fabian Affolter <fabian@bernewireless.net> - 1.90-1
- Updated to new upstream release 1.90

* Wed Jun 08 2011 Fabian Affolter <fabian@bernewireless.net> - 0.99-1
- Updated to new upstream release 0.99

* Sat Jun 04 2011 Fabian Affolter <fabian@bernewireless.net> - 0.9-2
- Scriplet updated
- Version condition removed

* Thu Jun 02 2011 Fabian Affolter <fabian@bernewireless.net> - 0.9-1
- Initial package for Fedora
