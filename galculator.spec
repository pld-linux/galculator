Summary:	a GTK 2 based scientific calculator
Summary(pl):	Kalkulator naukowy bazuj±cy na GTK 2
Name:		galculator
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://members.vol.at/home.floery/electronix/%{name}/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	26e41318ffef7c8341d14b166da0ebe8
Patch0:		%{name}-desktop.patch
URL:		http://members.vol.at/home.floery/electronix/galculator/home.html
BuildRequires:	gtk+2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK 2 based scientific calculator with ordinary notation/reverse
polish notation, different number bases (DEC, HEX, OCT, BIN) and
different angle bases (DEG, RAD, GRAD).

%description -l pl
Kalkulator naukowy bazuj±cy na GTK 2 z notacj± zwyk³± i odwrotn±
polsk±, ró¿nymi systemami liczbowymi (dziesiêtny, szesnastkowy,
ósemkowy, binarny) i ró¿nymi miarami k±towymi (stopieñ, radian,
gradus).

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_datadir}/applications

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz
