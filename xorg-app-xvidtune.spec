Summary:	xvidtune application
Summary(pl):	Aplikacja xvidtune
Name:		xorg-app-xvidtune
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xvidtune-%{version}.tar.bz2
# Source0-md5:	5addaae05c1aee5fcb457bc177476cf4
Patch0:		xvidtune-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xstdcmap application.

%description -l pl
Aplikacja xstdcmap.

%prep
%setup -q -n xvidtune-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/X11/app-defaults/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
