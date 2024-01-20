#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Validating URI References per RFC 3986
Summary(pl.UTF-8):	Sprawdzanie poprawności URI według RFC 3986
Name:		python-rfc3986
# keep 1.x here for python2 support
Version:	1.5.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/r/rfc3986/rfc3986-%{version}.tar.gz
# Source0-md5:	0e3a03c3eb3b679d5a253b168bb5774a
URL:		https://pypi.org/project/rfc3986
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-sphinx-prompt
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python implementation of RFC 3986 including validation and authority
parsing.

%description -l pl.UTF-8
Pythonowa implementacja RFC 3986 obejmująca sprawdzanie poprawności i
analizę wiarygodności.

%package -n python3-rfc3986
Summary:	Validating URI References per RFC 3986
Summary(pl.UTF-8):	Sprawdzanie poprawności URI według RFC 3986
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-rfc3986
A Python implementation of RFC 3986 including validation and authority
parsing.

%description -n python3-rfc3986 -l pl.UTF-8
Pythonowa implementacja RFC 3986 obejmująca sprawdzanie poprawności i
analizę wiarygodności.

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
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
sphinx-build-2 docs/source docs/build/html
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
%doc AUTHORS.rst LICENSE README.rst
%{py_sitescriptdir}/rfc3986
%{py_sitescriptdir}/rfc3986-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-rfc3986
%defattr(644,root,root,755)
%doc AUTHORS.rst LICENSE README.rst
%{py3_sitescriptdir}/rfc3986
%{py3_sitescriptdir}/rfc3986-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,api-ref,release-notes,user,*.html,*.js}
%endif
