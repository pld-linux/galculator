Summary:	A GTK+ 2 based scientific calculator
Summary(pl.UTF-8):	Kalkulator naukowy bazujący na GTK+ 2
Name:		galculator
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/galculator/%{name}-%{version}.tar.bz2
# Source0-md5:	f2de87209d4c9f8dc2fdb1d7a045bef2
Patch0:		%{name}-desktop.patch
URL:		http://galculator.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ 2 based scientific calculator with ordinary notation/reverse
polish notation, different number bases (DEC, HEX, OCT, BIN) and
different angle bases (DEG, RAD, GRAD).

%description -l pl.UTF-8
Kalkulator naukowy bazujący na GTK+ 2 z notacją zwykłą i odwrotną
polską, różnymi systemami liczbowymi (dziesiętny, szesnastkowy,
ósemkowy, binarny) i różnymi miarami kątowymi (stopień, radian,
gradus).

%prep
%setup -q -n %{name}-%{version}.0
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_pixmapsdir}/%{name}
