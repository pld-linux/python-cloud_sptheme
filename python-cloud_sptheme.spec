# TODO: docs (requires custom sphinxcontrib-fulltoc, see docs/requirements.txt)
#
# Conditional build:
%bcond_with	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	"Cloud" Sphinx Theme
Summary(pl.UTF-8):	Motyw "Cloud" dla Sphinksa
Name:		python-cloud_sptheme
Version:	1.9.4
Release:	2
License:	BSD
Group:		Libraries/Python
# if pypi:
#Source0Download: https://pypi.org/simple/cloud_sptheme/
Source0:	https://files.pythonhosted.org/packages/source/c/cloud_sptheme/cloud_sptheme-%{version}.tar.gz
# Source0-md5:	9a74d8609cd2c640c3a2ec459e5438dc
Patch0:		%{name}-mock.patch
URL:		https://pypi.org/project/cloud_sptheme/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.4
BuildRequires:	python-mock
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.4
%endif
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg
# python-sphinxcontrib-fulltoc
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small package containing a Sphinx theme named "Cloud", along
with some related Sphinx extensions.

%description -l pl.UTF-8
Ten mały pakiet zawiera motyw Sphinksa "Cloud" wraz z kilkoma
powiązanymi rozszerzeniami Sphinksa.

%package -n python3-cloud_sptheme
Summary:	"Cloud" Sphinx Theme
Summary(pl.UTF-8):	Motyw "Cloud" dla Sphinksa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-cloud_sptheme
This is a small package containing a Sphinx theme named "Cloud", along
with some related Sphinx extensions.

%description -n python3-cloud_sptheme -l pl.UTF-8
Ten mały pakiet zawiera motyw Sphinksa "Cloud" wraz z kilkoma
powiązanymi rozszerzeniami Sphinksa.

%package apidocs
Summary:	API documentation for Python cloud_sptheme module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona cloud_sptheme
Group:		Documentation

%description apidocs
API documentation for Python cloud_sptheme module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona cloud_sptheme.

%prep
%setup -q -n cloud_sptheme-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
%{__make} -C docs -j1 html
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
%doc CHANGES LICENSE README
%{py_sitescriptdir}/cloud_sptheme
%{py_sitescriptdir}/cloud_sptheme-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-cloud_sptheme
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%{py3_sitescriptdir}/cloud_sptheme
%{py3_sitescriptdir}/cloud_sptheme-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
