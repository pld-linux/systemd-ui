Summary:	Graphical frontend for systemd
Summary(pl.UTF-8):	Graficzny interfejs do systemd
Name:		systemd-ui
Version:	1
Release:	1
License:	GPL v2+
Group:		Applications/System
URL:		http://www.freedesktop.org/wiki/Software/systemd
Source0:	http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.xz
# Source0-md5:	aa481542e39639ab2236344ad96038fe
BuildRequires:	desktop-file-utils
BuildRequires:	glib2-devel >= 1:2.26.1
BuildRequires:	gtk+2-devel >= 2:2.24.0
BuildRequires:	libgee-devel
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 0.11
# not required for building from release (which contains *.c for *.vala)
#BuildRequires:	vala >= 0.10.0
Requires:	dbus(org.freedesktop.Notifications)
Requires:	polkit
Obsoletes:	systemd-gtk < 44-5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical front-end for systemd. It provides a simple user interface
to manage services, and a graphical agent to request passwords from
the user.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Categories not ; terminated, this fixes it :)
desktop-file-install --delete-original  \
	--dir=$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_desktopdir}/systemadm.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/systemadm
%attr(755,root,root) %{_bindir}/systemd-gnome-ask-password-agent
%{_mandir}/man1/systemadm.1*
%{_desktopdir}/systemadm.desktop
