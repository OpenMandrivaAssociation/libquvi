%define major 7
%define libname %mklibname quvi %{major}
%define devname %mklibname -d quvi

Summary:	Library for parsing flash media stream URLs with C API
Name:		libquvi
Version:	0.4.1
Release:	23
Group:		Networking/Other
License:	LGPLv2+
Url:		https://quvi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
Patch0:		libquvi-0.4.1-automake.patch
BuildRequires:	pkgconfig(libcurl) >= 7.18.2
BuildRequires:	libquvi-scripts-devel >= 0.4.21
BuildRequires:	pkgconfig(lua) >= 5.2.4
BuildRequires:	gettext-devel

%description
libquvi is a library for parsing video download links with C API.
It is written in C and intended to be a cross-platform library.

%package -n %{libname}
Summary:	Shared library files libquvi
Group:		Networking/Other
Requires:	libquvi-scripts >= 0.4.21

%description -n %{libname}
Shared library files libquvi.

%package -n %{devname}
Summary:	Files needed for building applications with libquvi
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	quvi-devel = %{EVRD}

%description -n %{devname}
Files needed for building applications with libquvi.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_includedir}/quvi
%{_includedir}/quvi/*
%{_mandir}/man3/*
