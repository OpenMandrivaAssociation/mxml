%define	major 1
%define libname	%mklibname mxml %{major}
%define develname %mklibname -d mxml

Summary:	Miniature XML development library
Name:		mxml
Version:	2.4
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.minixml.org/
Source0:	http://www.minixml.org/software.php?VERSION=2.3&FILE=mxml/%version/mxml-%{version}.tar.gz
BuildRequires:	chrpath
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

%package -n	%develname
Summary:	Static library and header files for the Miniature XML development library
Group:		Development/C
Provides:	libmxml-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes: %mklibname -d mxml 1

%description -n	%develname
This package contains the static mxml library and its header files.

%prep

%setup -q

%build
%configure2_5x \
	--enable-shared

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std BUILDROOT=%{buildroot}

mv %{buildroot}%{_datadir}/doc/mxml installed-docs

rm -rf %{buildroot}%{_mandir}/cat*

chrpath -d %{buildroot}%{_libdir}/*.so.%{major}*
chrpath -d %{buildroot}%{_bindir}/mxmldoc

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(644,root,root,755)
%doc ANNOUNCEMENT CHANGES COPYING README doc/*.html
%attr(755,root,root) %{_libdir}/*.so.%{major}*

%files -n %develname
%defattr(644,root,root,755)
%doc installed-docs/*
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/mxml.pc
%{_mandir}/man1/*
%{_mandir}/man3/*
