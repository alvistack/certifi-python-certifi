%global debug_package %{nil}

Name: python-certifi
Epoch: 100
Version: 2021.05.30
Release: 1%{?dist}
BuildArch: noarch
Summary: Python package for providing Mozilla's CA Bundle
License: MPL-2.0
URL: https://github.com/certifi/python-certifi/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Certifi is a carefully curated collection of Root Certificates for
validating the trustworthiness of SSL certificates while verifying the
identity of TLS hosts. It has been extracted from the Requests project.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-certifi
Summary: Python package for providing Mozilla's CA Bundle
Requires: python3
Provides: python3-certifi = %{epoch}:%{version}-%{release}
Provides: python3dist(certifi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-certifi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(certifi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-certifi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(certifi) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-certifi
Certifi is a carefully curated collection of Root Certificates for
validating the trustworthiness of SSL certificates while verifying the
identity of TLS hosts. It has been extracted from the Requests project.

%files -n python%{python3_version_nodots}-certifi
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-certifi
Summary: Python package for providing Mozilla's CA Bundle
Requires: python3
Provides: python3-certifi = %{epoch}:%{version}-%{release}
Provides: python3dist(certifi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-certifi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(certifi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-certifi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(certifi) = %{epoch}:%{version}-%{release}

%description -n python3-certifi
Certifi is a carefully curated collection of Root Certificates for
validating the trustworthiness of SSL certificates while verifying the
identity of TLS hosts. It has been extracted from the Requests project.

%files -n python3-certifi
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
