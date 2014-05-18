#
# Conditional build:
%bcond_with	gtk3	# use GTK+ 3.x instead of 2.x

Summary:	A GTK+ 2 based scientific calculator
Summary(pl.UTF-8):	Kalkulator naukowy bazujący na GTK+ 2
Name:		galculator
Version:	2.1.2
Release:	2
License:	GPL v2+
Group:		Applications/Math
Source0:	http://downloads.sourceforge.net/galculator/%{name}-%{version}.tar.bz2
# Source0-md5:	01c97ec3e18c26c64af78dca9f700d43
Patch0:		%{name}-desktop.patch
URL:		http://galculator.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libglade2-devel >= 1:2.0.1
BuildRequires:	pkgconfig
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
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
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{__enable_disable gtk3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{da_DK,da}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{kk_KZ,kk}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
%{_iconsdir}/hicolor/*/apps/galculator.png
%{_iconsdir}/hicolor/*/apps/galculator.svg
