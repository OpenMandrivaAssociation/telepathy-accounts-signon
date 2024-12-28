Name:		telepathy-accounts-signon
Summary:	Telepathy integration for the Accounts SSO framework
Version:	2.1
Release:	4
License:	LGPLv2+
Group:		Networking/Instant messaging
URL:		https://gitlab.com/accounts-sso/%{name}
Source0:	https://gitlab.com/accounts-sso/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	meson
BuildRequires:	pkgconfig(mission-control-plugins)
BuildRequires:	pkgconfig(libaccounts-glib)
BuildRequires:	pkgconfig(libsignon-glib) >= 2.0
BuildRequires:	pkgconfig(signond)

%description
A mission control plugin for Telepathy, integrating with libaccounts and libsignon
to provide IM accounts and authentication.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING.LGPL
%doc README.md
%{_libdir}/mission-control-plugins.0/*.so
