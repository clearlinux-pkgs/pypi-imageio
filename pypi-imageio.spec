#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-imageio
Version  : 2.31.3
Release  : 90
URL      : https://files.pythonhosted.org/packages/60/49/aaa7c876f81e3b689c14e117295439155aedb602034e74d94280c3378eb8/imageio-2.31.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/60/49/aaa7c876f81e3b689c14e117295439155aedb602034e74d94280c3378eb8/imageio-2.31.3.tar.gz
Summary  : Library for reading and writing a wide range of image, video, scientific, and volumetric data formats.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-imageio-bin = %{version}-%{release}
Requires: pypi-imageio-python = %{version}-%{release}
Requires: pypi-imageio-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(numpy)
BuildRequires : pypi(pillow)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# IMAGEIO
[![CI](https://github.com/imageio/imageio/workflows/CI/badge.svg)](https://github.com/imageio/imageio/actions/workflows/ci.yml)
[![CD](https://github.com/imageio/imageio/workflows/CD/badge.svg)](https://github.com/imageio/imageio/actions/workflows/cd.yml)
[![codecov](https://codecov.io/gh/imageio/imageio/branch/master/graph/badge.svg?token=81Zhu9MDec)](https://codecov.io/gh/imageio/imageio)
[![Docs](https://readthedocs.org/projects/imageio/badge/?version=latest)](https://imageio.readthedocs.io)

%package bin
Summary: bin components for the pypi-imageio package.
Group: Binaries

%description bin
bin components for the pypi-imageio package.


%package python
Summary: python components for the pypi-imageio package.
Group: Default
Requires: pypi-imageio-python3 = %{version}-%{release}

%description python
python components for the pypi-imageio package.


%package python3
Summary: python3 components for the pypi-imageio package.
Group: Default
Requires: python3-core
Provides: pypi(imageio)
Requires: pypi(numpy)
Requires: pypi(pillow)

%description python3
python3 components for the pypi-imageio package.


%prep
%setup -q -n imageio-2.31.3
cd %{_builddir}/imageio-2.31.3
pushd ..
cp -a imageio-2.31.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693931839
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/imageio_download_bin
/usr/bin/imageio_remove_bin

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
