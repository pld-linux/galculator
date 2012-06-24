Summary:	a GTK 2 based scientific calculator
Summary(pl):	Kalkulator naukowy bazuj�cy na GTK 2
Name:		galculator
Version:	1.0
Release:	0.rc1.1
License:	GPL
Group:		Applications/Math
Source0:	http://members.vol.at/home.floery/electronix/%{name}/downloads/%{name}-%{version}rc1.tar.bz2
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
Kalkulator naukowy bazuj�cy na GTK 2 z notacj� zwyk�� i odwrotn�
polsk�, r�nymi systemami liczbowymi (dziesi�tny, szesnastkowy,
�semkowy, binarny) i r�nymi miarami k�towymi (stopie�, radian,
gradus).

%prep
%setup -q -n %{name}-%{version}rc1
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
