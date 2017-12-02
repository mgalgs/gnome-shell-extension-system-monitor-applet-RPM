%global extuuid    system-monitor@paradoxxx.zero.gmail.com
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    gnome-shell-system-monitor-applet
%global giturl     https://github.com/paradoxxxzero/%{gitname}


Name:           gnome-shell-extension-system-monitor-applet
Epoch:          1
Version:        33
Release:        1%{?dist}
Summary:        A Gnome shell system monitor extension

# The entire source code is GPLv3+ except convenience.js, which is BSD
License:        GPLv3+ and BSD
URL:            https://extensions.gnome.org/extension/120/system-monitor/
Source0:        %{giturl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common

# CentOS 7 build environment doesn't support Recommends tag.
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     gnome-tweak-tool
%endif

%description
Display system information in gnome shell status bar, such as memory usage,
CPU usage, and network rate...


%prep
%autosetup -n %{gitname}-%{version} -p 1


%build
%make_build


%install
%make_install

# Cleanup crap.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}

# Install schema.
%{__mkdir} -p %{buildroot}%{gschemadir}
%{__cp} -pr %{extuuid}/schemas/*gschema.xml %{buildroot}%{gschemadir}

# Install i18n.
%{_bindir}/find %{extuuid} -name '*.po' -print -delete
%{__cp} -pr %{extuuid}/locale %{buildroot}%{_datadir}

# Create manifest for i18n.
%find_lang %{name} --all-name


# CentOS 7 doesn't compile gschemas automatically, Fedora does.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif


%files -f %{name}.lang
%doc README.md
%license COPYING
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
* Sat Dec 02 2017 Björn Esser <besser82@fedoraproject.org> - 1:33-1
- New upstream release
- Follow upstream versioning
- Bump Epoch since previous people messed up the versioning scheme
- Simplify packaging

* Tue Oct 24 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0-0.3.20171005git61b0a60
- Add support for EPEL 7.
- Revert upstream requires - Works with fresh vanilla Fedora with gnome-shell.

* Tue Oct 24 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0-0.2.20171005git61b0a60
- Requires libgtop2 and NetworkManager-glib
- Fix NVidia GPU support
- Spec file rework

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
