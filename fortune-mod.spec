# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       fortune-mod

# >> macros
# << macros
%define cookiedir %{_datadir}/fortune
%define localdir ${CMAKE_INSTALL_PREFIX}/local/games/fortunes

Summary:    a version of the UNIX fortune command
Version:    3.14.1
Release:    0
Group:      Applications
License:    ASL 2.0
URL:        https://github.com/nephros/fortune-mod
Source0:    https://github.com/shlomif/fortune-mod/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source100:  fortune-mod.yaml
Source101:  fortune-mod-rpmlintrc
Patch0:     %{name}-%{version}-fix-localdir-mixup.patch
BuildRequires:  perl
BuildRequires:  qml-rpm-macros
BuildRequires:  recode-devel
BuildRequires:  cmake

%description

fortune is a command-line utility which displays a random quotation from a
collection of quotes. This collection is read from the local file system
and does not require network access. A large collection of quotes is
provided in the download and installed by default, but more quote
collections can be added by the user.

%if "%{?vendor}" == "chum"
PackageName: fortune
Type: console-application
PackagerName: nephros
Categories:
 - Games
Custom:
  Repo: %{url}
Icon: %{url}/master/icons/template.svg
Url:
  Homepage: https://www.shlomifish.org/open-source/projects/fortune-mod/
  Bugtracker: %{url}/issues
  Donations:
    - https://noyb.eu/en/donations-other-support-options
    - https://my.fsfe.org/donate
    - https://supporters.eff.org/donate/join-4
    - https://openrepos.net/donate
%endif


%prep
%setup -q -n %{name}-%{version}

# %{name}-%{version}-fix-localdir-mixup.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
mkdir build
pushd build
%cmake .. \
  -DCOOKIEDIR=%{cookiedir} \
  -DLOCALDIR=%{localdir}
# << build pre

make %{?_smp_mflags}

# >> build post
popd
# << build post

%install
rm -rf %{buildroot}
# >> install pre
pushd build
# << install pre
%make_install

# >> install post
popd
# << install post

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/*
# >> files
# << files
