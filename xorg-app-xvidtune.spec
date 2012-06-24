Summary:	xvidtune application
Summary(pl):	Aplikacja xvidtune
Name:		xorg-app-xvidtune
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/app/xvidtune-%{version}.tar.bz2
# Source0-md5:	676e5ad5b8e9299a2945d070165bf956
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xvidtune application.

%description -l pl
Aplikacja xvidtune.

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
	DESTDIR=$RPM_BUILD_ROOT \
	appmandir=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/*
%{_mandir}/man1/*.1x*
