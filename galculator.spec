Summary:	a GTK 2 based scientific calculator
Summary(pl):	Kalkulator naukowy bazuj�cy na GTK 2
Name:		galculator
Version:	1.1.2
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	326b862122de170c53f44acf901327e7
URL:		http://galculator.sourceforge.net/
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
%setup -q

%build
%{__autoconf}
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
%attr(755,root,root)%{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.gz
