Summary:	OpenSync data synchronization commandline program
Summary(pl.UTF-8):	Programy do synchronizacji danych OpenSync
Name:		osynctool
Version:	0.39
Release:	1
License:	GPL
Group:		Applications
Source0:	http://opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	2fdf7ef8b23c0f948b7bd250da16aa0f
URL:		http://www.opensync.org/
BuildRequires:	cmake
BuildRequires:	libopensync-devel >= 1:0.39
BuildRequires:	pkgconfig
Obsoletes:	msynctool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

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
mkdir build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# no package yet
rm $RPM_BUILD_ROOT%{_prefix}/etc/bash_completion.d/osynctool.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/%{name}
