Name:		libudt
Version:	4.11
Release:	3%{?dist}
Summary:	UDP based application level data transport protocol

Group:		Development/Libraries
License:	BSD
URL:		http://udt.sf.net

Source:		https://github.com/asenci/udt/archive/v%{version}.tar.gz

BuildRequires:	make
BuildRequires:  gcc
BuildRequires:  gcc-c++

ExclusiveOS:	linux
ExclusiveArch:	x86_64

%description
UDT is a reliable UDP based application level data transport protocol for
distributed data intensive applications over wide area high-speed networks


%prep
%setup -q -c

%build
pushd udt-%{version}/src
%{__make} -e os=LINUX arch=AMD64

%install
%{__install} -d %{buildroot}%{_libdir}
%{__install} udt-%{version}/src/libudt.a %{buildroot}%{_libdir}
%{__install} udt-%{version}/src/libudt.so %{buildroot}%{_libdir}
%{__install} -d %{buildroot}%{_includedir}
%{__install} udt-%{version}/src/udt.h %{buildroot}%{_includedir}
%{__install} -d %{buildroot}%{_includedir}/udt
%{__install} udt-%{version}/src/*.h %{buildroot}%{_includedir}/udt

%files
%defattr(644,root,root,755)
%{_libdir}/libudt.so

%clean
%{__rm} -rf %{buildroot}


# Development
%package devel
Summary:        Headers and libraries for building apps using UDT library

BuildArch:	noarch

Requires:       %{name} = %{version}-%{release}

%description devel
This package contains headers and libraries required to build applications that
use the UDT library.

%files devel
%defattr(644,root,root,755)
%{_libdir}/libudt.a
%{_includedir}/udt
%{_includedir}/udt.h


# Changelog
%changelog
* Thu Apr 02 2020 Andre Sencioles <asenci@gmail.com> - 4.11-1
- Initial release
