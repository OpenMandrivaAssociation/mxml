%define	major 1
%define libname	%mklibname mxml %{major}

Summary:	Miniature XML development library
Name:		mxml
Version:	2.2.2
Release:	%mkrel 2
License:	GPL
Group:		System/Libraries
URL:		http://www.easysw.com/~mike/mxml/
Source0:	ftp://ftp3.easysw.com/pub/mxml/%{version}/mxml-%{version}.tar.bz2
Patch0:		mxml-2.2.2-shared.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Mini-XML is a small XML parsing library that you can use to read XML and
XML-like data files in your application without requiring large non-standard
libraries.  Mini-XML provides the following functionality:

- Reading of UTF-8 and UTF-16 and writing of UTF-8 encoded  XML files and
  strings.
- Data is stored in a linked-list tree structure, preserving  the XML data
  hierarchy.
- Supports arbitrary element names, attributes, and attribute values with no
  preset limits, just available memory.
- Supports integer, real, opaque ("cdata"), and text data types in "leaf"
  nodes.
- Functions for creating and managing trees of data.
- "Find" and "walk" functions for easily locating and navigating trees of data.

Mini-XML doesn't do validation or other types of processing on the data based
upon schema files or other sources of definition information, nor does it
support character entities other than those required by the XML specification.

%package -n	%{libname}
Summary:	Miniature XML development library
Group:          System/Libraries

%description -n	%{libname}
Mini-XML is a small XML parsing library that you can use to read XML and
XML-like data files in your application without requiring large non-standard
libraries.  Mini-XML provides the following functionality:

- Reading of UTF-8 and UTF-16 and writing of UTF-8 encoded  XML files and
  strings.
- Data is stored in a linked-list tree structure, preserving  the XML data
  hierarchy.
- Supports arbitrary element names, attributes, and attribute values with no
  preset limits, just available memory.
- Supports integer, real, opaque ("cdata"), and text data types in "leaf"
  nodes.
- Functions for creating and managing trees of data.
- "Find" and "walk" functions for easily locating and navigating trees of data.

Mini-XML doesn't do validation or other types of processing on the data based
upon schema files or other sources of definition information, nor does it
support character entities other than those required by the XML specification.

%package -n	%{libname}-devel
Summary:	Static library and header files for the Miniature XML development library
Group:		Development/C
Obsoletes:	%{name}-devel
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
This package contains the static mxml library and its header files.

%prep

%setup -q
%patch0 -p1

%build

export CFLAGS="%{optflags} -fPIC"

./configure \
    --prefix=%{_prefix} \
    --exec-prefix=%{_exec_prefix} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --sysconfdir=%{_sysconfdir} \
    --datadir=%{_datadir} \
    --includedir=%{_includedir} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libexecdir} \
    --localstatedir=%{_localstatedir} \
    --sharedstatedir=%{_sharedstatedir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --enable-shared

make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std BUILDROOT=%{buildroot}

mv %{buildroot}%{_datadir}/doc/mxml installed-docs

rm -rf %{buildroot}%{_datadir}/man/cat*

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc ANNOUNCEMENT CHANGES COPYING README doc/*.html
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc installed-docs/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/mxml.pc
%{_mandir}/man1/*
%{_mandir}/man3/*


