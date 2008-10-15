Summary:	OpenSync data synchronization commandline programs
Summary(pl.UTF-8):	Programy do synchronizacji danych OpenSync
Name:		msynctool
Version:	0.37
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	417d582a1c2ac1049b41557ee5664f3e
URL:		http://opensync.org/
BuildRequires:	cmake
BuildRequires:	libopensync-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and distribution
independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains commandline programs to use OpenSync framework.

%description -l pl.UTF-8
OpenSync to niezależny od platformy i dystrybucji szkielet do
synchronizacji danych.

Składa się z różnych wtyczek, których można używać do łączenia z
urządzeniami, potężnego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera działające z linii poleceń programy do korzystania
ze szkieletu OpenSync.

%prep
%setup -q

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	.
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS 
%attr(755,root,root) %{_bindir}/*
