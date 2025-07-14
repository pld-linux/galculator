#
# Conditional build:
%bcond_without	gtk3	# use GTK+ 3.x instead of 2.x

Summary:	A GTK+3 based scientific calculator
Summary(pl.UTF-8):	Kalkulator naukowy bazujący na GTK+3
Name:		galculator
Version:	2.1.4
Release:	1
License:	GPL v2+
Group:		Applications/Math
Source0:	http://galculator.mnim.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	1a115d6799dc453a29760e7bd4a56374
Patch0:		%{name}-desktop.patch
URL:		http://galculator.mnim.org
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
GTK+3 based scientific calculator with ordinary notation/reverse
polish notation, different number bases (DEC, HEX, OCT, BIN) and
different angle bases (DEG, RAD, GRAD).

%description -l pl.UTF-8
Kalkulator naukowy bazujący na GTK+3 z notacją zwykłą i odwrotną
polską, różnymi systemami liczbowymi (dziesiętny, szesnastkowy,
ósemkowy, binarny) i różnymi miarami kątowymi (stopień, radian,
gradus).

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
# workaround for GCC10 build failure
export CFLAGS="%(echo %{optflags}) -fcommon"
export CXXFLAGS="$CFLAGS"
%configure \
	%{__enable_disable gtk3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_datadir}/appdata/galculator.appdata.xml
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
%{_iconsdir}/hicolor/*/apps/galculator.png
%{_iconsdir}/hicolor/*/apps/galculator.svg
