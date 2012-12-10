%define	major 1
%define libname	%mklibname mxml %{major}
%define develname %mklibname -d mxml

Summary:	Miniature XML development library
Name:		mxml
Version:	2.7
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.minixml.org/
Source0:	http://ftp.easysw.com/pub/mxml/%version/mxml-%{version}.tar.gz
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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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


%changelog
* Fri Dec 30 2011 Götz Waschk <waschk@mandriva.org> 2.7-1mdv2012.0
+ Revision: 748225
- update to new version 2.7

* Wed Jul 13 2011 Götz Waschk <waschk@mandriva.org> 2.6-2
+ Revision: 689836
- rebuild

* Mon Jun 08 2009 Götz Waschk <waschk@mandriva.org> 2.6-1mdv2011.0
+ Revision: 383920
- new version
- fix source URL

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2.5-3mdv2009.0
+ Revision: 253406
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Jan 31 2008 Götz Waschk <waschk@mandriva.org> 2.5-1mdv2008.1
+ Revision: 160646
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 24 2007 Götz Waschk <waschk@mandriva.org> 2.4-1mdv2008.1
+ Revision: 111769
- new version

* Mon Oct 22 2007 Götz Waschk <waschk@mandriva.org> 2.3-1mdv2008.1
+ Revision: 101117
- new devel name
- fix URL
- fix license

  + Thierry Vignaud <tv@mandriva.org>
    - replace %%{_datadir}/man by %%{_mandir}!

* Sat Apr 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.3-1mdv2008.0
+ Revision: 18974
- new version
- drop P0
- use macros
- remove rpath
- drop provides and obsoletes from -devel


* Tue Oct 24 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-2mdv2007.0
+ Revision: 72133
- forgot to add the patch...
- new major
- make it a shared lib
- Import mxml

* Mon May 29 2006 Götz Waschk <waschk@mandriva.org> 2.2.2-1mdv2007.0
- Rebuild

* Thu May 26 2005 G�tz Waschk <waschk@mandriva.org> 2.2.2-1mdk
- New release 2.2.2

* Sat Apr 16 2005 G�tz Waschk <waschk@linux-mandrake.com> 2.2-1mdk
- source URL
- New release 2.2

* Mon Jul 19 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.0-1mdk
- initial package

