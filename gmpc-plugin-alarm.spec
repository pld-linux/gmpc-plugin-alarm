%define		source_name gmpc-alarm
Summary:	gmpc-alarm - basic timer plugin for gmpc
Name:		gmpc-plugin-alarm
Version:	11.8.16
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{source_name}-%{version}.tar.gz
# Source0-md5:	d421bc55b5ee879933dddcda661eb3ca
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_ALARM
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	gmpc-devel >= 0.18.1
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	intltool
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Alarm Timer plugin turns your music player into an alarm, set the
time in at which it must go off and the rest is done by gmpc.

You can set the time on which gmpc should go off and set an action
that gmpc should execute when the alarm goes off.

%prep
%setup -qn %{source_name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%find_lang gmpc-alarm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gmpc-alarm.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/gmpc/plugins/alarmplugin.so
%{_datadir}/gmpc-alarm
