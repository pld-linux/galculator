Summary:	A GTK 2 based scientific calculator
Summary(pl):	Kalkulator naukowy bazuj±cy na GTK 2
Name:		galculator
Version:	1.1.4
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	3f0d80474ef6c585958e5ece5f6d5aa7
Patch0:		%{name}-desktop.patch
URL:		http://galculator.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	libglade2-devel >= 2.0.1
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
