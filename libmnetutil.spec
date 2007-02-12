#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	libmnetutil - different utilities classes for portable networking C++ development
Summary(pl.UTF-8):   libmnetutil - różne klasy narzędziowe dla przenośnej obsługi sieci w C++
Name:		libmnetutil
Version:	0.3.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.minisip.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	1454b0adc907fb02f88414e9e1a58ec0
URL:		http://www.minisip.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libmutil-devel >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmnetutil contains different classes useful to write portable
networking applications in C++. It includes UDP, TCP and TLS sockets,
DNS resolving etc.

%description -l pl.UTF-8
Biblioteka libmnetutil zawiera różne klasy przydatne do pisania
przenośnych aplikacji sieciowych w C++. Obejmuje gniazda UDP, TCP i
TLS, rozwiązywanie DNS itp.

%package devel
Summary:	Header files for libmnetutil library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libmnetutil
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libmutil-devel >= %{version}

%description devel
Header files for libmnetutil library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmnetutil.

%package static
Summary:	Static libmnetutil library
Summary(pl.UTF-8):   Statyczna biblioteka libmnetutil
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmnetutil library.

%description static -l pl.UTF-8
Statyczna biblioteka libmnetutil.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libmnetutil.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmnetutil.so
%{_libdir}/libmnetutil.la
%{_includedir}/libmnetutil

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmnetutil.a
%endif
