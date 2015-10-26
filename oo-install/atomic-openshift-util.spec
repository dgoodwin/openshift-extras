%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global import_path github.com/openshift/openshift-extras
# %commit is intended to be set by tito custom builders provided
# in the .tito/lib directory. The values in this spec file will not be kept up to date.
%{!?commit:
%global commit c64d09e528ca433832c6b6e6f5c7734a9cc8ee6f
}

Name:           atomic-openshift-util
Version:        3.0.0
Release:        1%{?dist}
Summary:        Atomic OpenShift Utilities
License:        ASL 2.0
URL:            http://github.com/openshift/openshift-extras/tree/enterprise-3.0/oo-install
Source0:        https://%{import_path}/archive/%{commit}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: python-setuptools
Requires:      ansible
Requires:      python-click
Requires:      python-ecdsa
Requires:      python-jinja2
Requires:      python-markupsafe
Requires:      python-paramiko
Requires:      python-crypto
Requires:      python-setuptools
Requires:      PyYAML

%description
Atomic OpenShift Utilities includes
 - atomic-openshift-installer
 - other utilities

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}
# Remove this line once the name change has happened
mv -f %{buildroot}%{_bindir}/oo-install %{buildroot}%{_bindir}/atomic-openshift-installer
mkdir -p %{buildroot}%{_datarootdir}/atomic-openshift-util/
cp etc/ansible.cfg %{buildroot}%{_datarootdir}/atomic-openshift-util/

# Uncomment once tests are working
#%check
#%{__python} ./tests/test_simple.py

%files
%{python_sitelib}/*
%{_bindir}/atomic-openshift-installer
%{_datarootdir}/atomic-openshift-util/ansible.cfg

%changelog
* Tue Oct 13 2015 Troy Dawson <tdawson@redhat.com> 3.0.0-1
- Initial Package

