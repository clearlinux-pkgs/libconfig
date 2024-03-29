#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libconfig
Version  : 1.7.3
Release  : 18
URL      : https://hyperrealm.github.io/libconfig/dist/libconfig-1.7.3.tar.gz
Source0  : https://hyperrealm.github.io/libconfig/dist/libconfig-1.7.3.tar.gz
Summary  : C Configuration File Library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libconfig-info = %{version}-%{release}
Requires: libconfig-lib = %{version}-%{release}
Requires: libconfig-license = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : flex

%description
To produce a PDF manual, issue the command "make pdf" after running
`./configure'.

%package dev
Summary: dev components for the libconfig package.
Group: Development
Requires: libconfig-lib = %{version}-%{release}
Provides: libconfig-devel = %{version}-%{release}
Requires: libconfig = %{version}-%{release}

%description dev
dev components for the libconfig package.


%package info
Summary: info components for the libconfig package.
Group: Default

%description info
info components for the libconfig package.


%package lib
Summary: lib components for the libconfig package.
Group: Libraries
Requires: libconfig-license = %{version}-%{release}

%description lib
lib components for the libconfig package.


%package license
Summary: license components for the libconfig package.
Group: Default

%description license
license components for the libconfig package.


%prep
%setup -q -n libconfig-1.7.3
cd %{_builddir}/libconfig-1.7.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624296801
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
(cd tests && ./libconfig_tests)

%install
export SOURCE_DATE_EPOCH=1624296801
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libconfig
cp %{_builddir}/libconfig-1.7.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/libconfig/7898de9d8a0026da533e44a786a17e435d7697f0
cp %{_builddir}/libconfig-1.7.3/contrib/ls-config/LICENSE %{buildroot}/usr/share/package-licenses/libconfig/10e16aac4efb91257b41fb884b7cec9af7b445b1
cp %{_builddir}/libconfig-1.7.3/contrib/ls-config/debian/copyright %{buildroot}/usr/share/package-licenses/libconfig/084bec6b51040315402fe44f484ce1fa09474c78
cp %{_builddir}/libconfig-1.7.3/contrib/ls-config/debian/ls-config/usr/share/doc/ls-config/copyright %{buildroot}/usr/share/package-licenses/libconfig/084bec6b51040315402fe44f484ce1fa09474c78
cp %{_builddir}/libconfig-1.7.3/debian/copyright %{buildroot}/usr/share/package-licenses/libconfig/8699b3b9540d45d5ca477cf8147589aa55957bc0
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libconfig.h
/usr/include/libconfig.h++
/usr/lib64/cmake/libconfig++/libconfig++Config.cmake
/usr/lib64/cmake/libconfig/libconfigConfig.cmake
/usr/lib64/libconfig++.so
/usr/lib64/libconfig.so
/usr/lib64/pkgconfig/libconfig++.pc
/usr/lib64/pkgconfig/libconfig.pc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libconfig.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libconfig++.so.11
/usr/lib64/libconfig++.so.11.1.0
/usr/lib64/libconfig.so.11
/usr/lib64/libconfig.so.11.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libconfig/084bec6b51040315402fe44f484ce1fa09474c78
/usr/share/package-licenses/libconfig/10e16aac4efb91257b41fb884b7cec9af7b445b1
/usr/share/package-licenses/libconfig/7898de9d8a0026da533e44a786a17e435d7697f0
/usr/share/package-licenses/libconfig/8699b3b9540d45d5ca477cf8147589aa55957bc0
