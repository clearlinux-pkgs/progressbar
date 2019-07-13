#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : progressbar
Version  : 2.5
Release  : 4
URL      : https://files.pythonhosted.org/packages/a3/a6/b8e451f6cff1c99b4747a2f7235aa904d2d49e8e1464e0b798272aa84358/progressbar-2.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/a3/a6/b8e451f6cff1c99b4747a2f7235aa904d2d49e8e1464e0b798272aa84358/progressbar-2.5.tar.gz
Summary  : Text progress bar library for Python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: progressbar-license = %{version}-%{release}
Requires: progressbar-python = %{version}-%{release}
Requires: progressbar-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Text progress bar library for Python.
A text progress bar is typically used to display the progress of a long
running operation, providing a visual cue that processing is underway.

%package license
Summary: license components for the progressbar package.
Group: Default

%description license
license components for the progressbar package.


%package python
Summary: python components for the progressbar package.
Group: Default
Requires: progressbar-python3 = %{version}-%{release}

%description python
python components for the progressbar package.


%package python3
Summary: python3 components for the progressbar package.
Group: Default
Requires: python3-core

%description python3
python3 components for the progressbar package.


%prep
%setup -q -n progressbar-2.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547490691
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/progressbar
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/progressbar/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/progressbar/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
