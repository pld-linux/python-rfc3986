#
# Conditional build:
%bcond_with	doc	# do build doc (broken)
%bcond_with	tests	# do perform "make test" (broken)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Validating URI References per RFC 3986
Name:		python-rfc3986
Version:	1.1.0
Release:	5
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/r/rfc3986/rfc3986-%{version}.tar.gz
# Source0-md5:	fca89d6e949c31922ef82422ace66842
URL:		https://pypi.python.org/pypi/rfc3986
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python implementation of RFC 3986 including validation and authority
parsing.

%package -n python3-rfc3986
Summary:	Validating URI References per RFC 3986
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-rfc3986
A Python implementation of RFC 3986 including validation and authority
parsing.

%package apidocs
Summary:	API documentation for Python rfc3986 module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona rfc3986
Group:		Documentation

%description apidocs
API documentation for Pythona rfc3986 module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona rfc3986.

%prep
%setup -q -n rfc3986-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst README.rst
%{py_sitescriptdir}/rfc3986
%{py_sitescriptdir}/rfc3986-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-rfc3986
%defattr(644,root,root,755)
%doc AUTHORS.rst README.rst
%{py3_sitescriptdir}/rfc3986
%{py3_sitescriptdir}/rfc3986-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
