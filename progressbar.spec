#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : progressbar
Version  : 2.5
Release  : 8
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

The ProgressBar class manages the current progress, and the format of the line
is given by a number of widgets. A widget is an object that may display
differently depending on the state of the progress bar. There are three types
of widgets:
 - a string, which always shows itself

 - a ProgressBarWidget, which may return a different value every time its
   update method is called

 - a ProgressBarWidgetHFill, which is like ProgressBarWidget, except it
   expands to fill the remaining width of the line.

The progressbar module is very easy to use, yet very powerful. It will also
automatically enable features like auto-resizing when the system supports it.

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
Provides: pypi(progressbar)

%description python3
python3 components for the progressbar package.


%prep
%setup -q -n progressbar-2.5
cd %{_builddir}/progressbar-2.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583203312
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/progressbar
cp %{_builddir}/progressbar-2.5/LICENSE.txt %{buildroot}/usr/share/package-licenses/progressbar/7b6fd4fb12f5faab38bf585461dd1a02da2e70f6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/progressbar/7b6fd4fb12f5faab38bf585461dd1a02da2e70f6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
