# Disable debuginfo as it causes issues with bundled gems that build libraries
%global debug_package %{nil}
%global repo_name bc-hcc-tensorboard
%global app_name bc_hcc_tensorboard
%{!?package_version: %define package_version _undefined.version_}
%{!?package_release: %define package_release 1}

Name:     ondemand-%{app_name}
Version:  %{package_version}
Release:  %{package_release}%{?dist}
Summary:  Batch Connect - HCC Tensorboard

Group:    System Environment/Daemons
License:  MIT
URL:      https://git.unl.edu/hcc/bc_hcc_desktop
Source0:  bc-hcc-tensorboard.tar.gz

BuildArch: noarch
Requires: ondemand

# Disable automatic dependencies as it causes issues with bundled gems and
# node.js packages used in the apps
AutoReqProv: no

%description
A Batch Connect app designed to launch a Tensorboard notebook within a batch job.


%prep
%setup -q -n %{repo_name}-%{package_version}


%build


%install
%__mkdir_p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}
%__cp -a ./. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}/
echo v%{version} > %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}/VERSION


%files
%defattr(-,root,root)
%{_localstatedir}/www/ood/apps/sys/%{app_name}
%{_localstatedir}/www/ood/apps/sys/%{app_name}/manifest.yml


%changelog
* Wed Feb 10 2021 Adam Caprez <acaprez2@unl.edu> v%{version}-%{release}
- initial version based off of https://github.com/OSC/bc_osc_jupyter/blob/master/packaging/ondemand-bc_osc_jupyter.spec
