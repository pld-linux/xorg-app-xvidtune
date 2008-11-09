Summary:	xvidtune application
Summary(pl.UTF-8):	Aplikacja xvidtune
Name:		xorg-app-xvidtune
Version:	1.0.1
Release:	4
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xvidtune-%{version}.tar.bz2
# Source0-md5:	e0744594f4e5969b20df28d897781318
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xvidtune application.

%description -l pl.UTF-8
Aplikacja xvidtune.

%prep
%setup -q -n xvidtune-%{version}

%build
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xvidtune
%{_datadir}/X11/app-defaults/Xvidtune
%{_mandir}/man1/xvidtune.1x*
