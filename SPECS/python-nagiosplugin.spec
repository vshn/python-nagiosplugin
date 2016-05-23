%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global srcname nagiosplugin

Name:           python-%{srcname}
Version:        1.2.4
Release:        1.vortex%{?dist}
Summary:        Class library for writing Nagios (Icinga) plugins
Vendor:         Vortex RPM

Group:          Development/Libraries
License:        ZPL
URL:            http://projects.gocept.com/projects/nagiosplugin
Source0:        http://pypi.python.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-setuptools, python-devel

%description
nagiosplugin is a Python class library which helps writing Nagios (or Icinga)
compatible plugins easily in Python. It cares for much of the boilerplate code
and default logic commonly found in Nagios checks, including:

- Nagios 3 Plugin API compliant parameters and output formatting
- Full Nagios range syntax support
- Automatic threshold checking
- Multiple independend measures
- Custom status line to communicate the main point quickly
- Long output and performance data
- Timeout handling
- Persistent "cookies" to retain state information between check runs
- Resume log file processing at the point where the last run left
- No dependencies beyond the Python standard library (except for Python 2.6).


nagiosplugin runs on POSIX and Windows systems. It is compatible with Python 3.3,
Python 3.2, Python 2.7, and Python 2.6.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt CONTRIBUTORS.txt HACKING.txt HISTORY.txt LICENSE.txt
%{python_sitelib}/%{srcname}*

%changelog
* Mon May 23 2016 Sam MCLeod <github.com/sammcj> - 1.2.4
* Sun May  4 2014 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 1.2.1-1.vortex
- Initial packaging.
