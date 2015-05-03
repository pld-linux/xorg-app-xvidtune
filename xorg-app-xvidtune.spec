Summary:	xvidtune application - video mode tuner for X server
Summary(pl.UTF-8):	Aplikacja xvidtune do strojenia trybów obrazu X serwera
Name:		xorg-app-xvidtune
Version:	1.0.3
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xvidtune-%{version}.tar.bz2
# Source0-md5:	8676c9bb1658fe91de244e850f6c3ca8
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xvidtune application is a client interface to the X server video mode
extension (XFree86-VidModeExtension).

%description -l pl.UTF-8
Aplikacja xvidtune to interfejs kliencki rozszerzenia trybów obrazu X
serwera (XFree86-VidModeExtension).

%prep
%setup -q -n xvidtune-%{version}

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xvidtune
%{_datadir}/X11/app-defaults/Xvidtune
%{_mandir}/man1/xvidtune.1*
