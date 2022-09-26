# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       fortune-mod

# >> macros
# << macros
%define cookiedir %{_datadir}/fortune
%define localdir %{_prefix}/local/games/fortune

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
Patch1:     games_to_bin.patch
BuildRequires:  cmake
BuildRequires:  perl
BuildRequires:  recode-devel

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


%package cookies
Summary:    Data files for %{name}
Group:      Games
Requires:   %{name} = %{version}-%{release}
Provides:   fortune-cookies

%description cookies
%{summary}.

%package offensive-cookies
Summary:    Data files for %{name}
Group:      Games
Requires:   %{name} = %{version}-%{release}
Provides:   fortune-cookies

%description offensive-cookies
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# %{name}-%{version}-fix-localdir-mixup.patch
%patch0 -p1
# games_to_bin.patch
%patch1 -p1
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
mkdir -p %{buildroot}/%{localdir}
rm -rf %{buildroot}/%{_mandir}
# << install post

%files
%defattr(-,root,root,-)
%license COPYING.txt
%{_bindir}/*
%dir %{cookiedir}
%dir %{localdir}
# >> files
# << files

%files cookies
%defattr(-,root,root,-)
%{cookiedir}/art*
%{cookiedir}/ascii-art*
%{cookiedir}/computers*
%{cookiedir}/cookie*
%{cookiedir}/debian*
%{cookiedir}/definitions*
%{cookiedir}/disclaimer*
%{cookiedir}/drugs*
%{cookiedir}/education*
%{cookiedir}/ethnic*
%{cookiedir}/food*
%{cookiedir}/fortunes*
%{cookiedir}/goedel*
%{cookiedir}/humorists*
%{cookiedir}/kids*
%{cookiedir}/knghtbrd*
%{cookiedir}/law*
%{cookiedir}/linux*
%{cookiedir}/literature*
%{cookiedir}/love*
%{cookiedir}/magic*
%{cookiedir}/medicine*
%{cookiedir}/miscellaneous*
%{cookiedir}/news*
%{cookiedir}/paradoxum*
%{cookiedir}/people*
%{cookiedir}/perl*
%{cookiedir}/pets*
%{cookiedir}/platitudes*
%{cookiedir}/politics*
%{cookiedir}/pratchett*
%{cookiedir}/riddles*
%{cookiedir}/rules-of-acquisition*
%{cookiedir}/science*
%{cookiedir}/songs-poems*
%{cookiedir}/sports*
%{cookiedir}/startrek*
%{cookiedir}/tao*
%{cookiedir}/translate-me*
%{cookiedir}/wisdom*
%{cookiedir}/work*
%{cookiedir}/zippy*
# >> files cookies
# << files cookies

%files offensive-cookies
%defattr(-,root,root,-)
%{cookiedir}/off/*
%{cookiedir}/men-women*
# >> files offensive-cookies
# << files offensive-cookies
