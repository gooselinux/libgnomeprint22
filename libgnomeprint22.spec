%define gettext_package libgnomeprint-2.2

%define glib2_base_version 2.2.0
%define glib2_version %{glib2_base_version}
%define pango_version 1.5.0
%define libxml2_version 2.5
%define libart_lgpl_version 2.3.8
%define libbonobo_version 2.1.0
%define bonobo_activation_version 1.0.0
%define freetype_version 2.0.3
%define gtk_doc_version 0.9

Summary: Printing library for GNOME
Name:		libgnomeprint22
Version: 	2.18.6
Release:	4%{?dist}
License:	LGPLv2+ and BSD
# BSD applies to ttsubset code that was taken from STSF
Group:          System Environment/Base
Source: 	http://download.gnome.org/sources/libgnomeprint/2.18/libgnomeprint-%{version}.tar.bz2
URL:            http://www.gnome.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	urw-fonts
Requires:	ghostscript
Requires:	ghostscript-fonts

BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	pango-devel >= %{pango_version}
BuildRequires:	libxml2-devel >= %{libxml2_version}
BuildRequires:	libart_lgpl-devel >= %{libart_lgpl_version}
BuildRequires:	libbonobo-devel >= %{libbonobo_version}
BuildRequires:	bonobo-activation-devel >= %{bonobo_activation_version}
BuildRequires:	freetype >= %{freetype_version}
BuildRequires:	gtk-doc >= %{gtk_doc_version}
BuildRequires:	libgnomecups-devel >= 0.2.0-1
BuildRequires:	fontconfig
BuildRequires:	cups-devel
BuildRequires:	intltool
BuildRequires:	zlib-devel
BuildRequires:  gnutls-devel
BuildRequires:  openssl-devel
BuildRequires:  gettext
BuildRequires:  bison
BuildRequires:  flex

# updated translations
# https://bugzilla.redhat.com/show_bug.cgi?id=589220
Patch0: libgnomeprint22-translations.patch

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. The gnome-print package contains
libraries and fonts needed by GNOME applications for printing.

You should install the gnome-print package if you intend to use any of
the GNOME applications that can print. If you would like to develop
GNOME applications that can print you will also need to install the
gnome-print devel package.

%package devel
Summary: Libraries and include files for developing GNOME printing applications
Group: Development/Libraries

Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
Requires:	glib2-devel >= %{glib2_version}
Requires:	pango-devel >= %{pango_version}
Requires:	libxml2-devel >= %{libxml2_version}
Requires:	libart_lgpl-devel >= %{libart_lgpl_version}
Requires:	libbonobo-devel >= %{libbonobo_version}
Requires:	bonobo-activation-devel >= %{bonobo_activation_version}
Requires:	freetype >= %{freetype_version}
# for /usr/share/gtk-doc/html
Requires:       gtk-doc

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. The gnome-print-devel package
includes the libraries and include files needed for developing
applications that use the GNOME printing capabilities.

You should install the gnome-print-devel package if you would like to
develop GNOME applications that will use the GNOME print capabilities.
You do not need to install the gnome-print-devel package if you just
want to use the GNOME desktop environment.

%prep
%setup -q -n libgnomeprint-%{version}
%patch0 -p1 -b .translations

%build
%configure --disable-rpath --disable-static --disable-gtk-doc
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name *.la -exec rm {} \;

%find_lang %{gettext_package}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{gettext_package}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/lib*.so.*
%{_libdir}/libgnomeprint/
%{_datadir}/libgnomeprint/

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/html/libgnomeprint

%changelog
* Wed Jun 23 2010 Matthias Clasen <mclasen@redhat.com> - 2.18.6-4
- Updated translations
Resolves: #589220

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.18.6-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Matthias Clasen <mclasen@redhat.com> - 2.18.6-2
- Rebuild

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.18.6-1
- Update to 2.18.6

* Mon Mar  9 2009  Peter Robinson <pbrobinson@gmail.com> - 2.18.5-3
- Remove redundent perl dep - RHBZ 489227

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.18.5-1
- Update to 2.18.5

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.18.4-2
- fix license tag

* Wed Feb 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.18.4-1
- Update to 2.18.4

* Tue Jan 29 2008 Matthias Clasen <mclasen@redhat.com> - 2.18.3-1
- Update to 2.18.3

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.2-1
- Update to 2.18.2

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 2.18.1-2
- Rebuild for build ID

* Sun Jul  8 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-3
- Update the license field
- Fix a directory ownership issue

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-2
- Don't ship .la files
- Require pkgconfig in the -devel package

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.92-1
- Update to 2.17.92

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.91-1
- Update to 2.17.91

* Tue Jan 23 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.90-1
- Update to 2.17.90

* Mon Nov 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.0-2
- Fix BuildRequires

* Sun Nov 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.0-1
- Update to 2.17.0

* Thu Jul 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.12.1-8
- Disable gtk-doc to fix multilib conflicts

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.12.1-7.1
- rebuild

* Wed Jun 14 2006 Tomas Mraz <tmraz@redhat.com> - 2.12.1-7
- rebuilt with new gnutls

* Mon Jun 12 2006 Bill Nottingham <notting@redhat.com> - 2.12.1-6
- buildreq automake, not automake16
- buildreq gettext, bison, flex

* Mon May 22 2006 Matthias Clasen <mclasen@redhat.com> - 2.12.1-5
- Add missing BuildRequires

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.12.1-4.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.12.1-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Dec 21 2005 Kristian Høgsberg <krh@redhat.com> 2.12.1-4
- Spec file clean-ups from from Matthias Saou (#172923):
  - Explicitly disable rpath.
  - Exclude static modules from the main package.
  - Exclude static libraries from the devel package (useless).
  - Don't own entire %{_datadir}/gtk-doc.
  - Remove explicit pre/post /sbin/ldconfig deps (they're automatic with -p).
  - Change PreReqs to more correct Requires.
  - Fix devel summary.
  - Add _smp_mflags to build.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov  9 2005 Tomas Mraz <tmraz@redhat.com> - 2.12.1-3
- rebuilt against new openssl

* Wed Oct  5 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.1-2
- Use gmodule-no-export in the .pc file

* Wed Sep 29 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.1-1
- Update to 2.12.1

* Wed Sep  7 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.0-1
- Update to 2.12.0

* Mon Jul 11 2005 Matthias Clasen <mclasen@redhat.com> - 2.11.0-1
- Newer upstream version

* Tue May 24 2005 David Zeuthen <davidz@redhat.com> - 2.10.3-1
- Update to upstream release 2.10.3 (#158397). Temporarily disable
  the fix for #154939 since that may be fixed upstream.

* Fri Apr 29 2005 John (J5) Palmieri <johnp@redhat.com> - 2.10.1-3
- Added patch to make sure glyphs are layed out right (Bug #154939)

* Fri Mar 18 2005 David Zeuthen <davidz@redhat.com> - 2.10.1-2
- Require libgnomecups >= 0.2.0-1 and rebuild

* Fri Mar 18 2005 David Zeuthen <davidz@redhat.com> - 2.10.1-1
- New upstream version; drop the async patches as they are now upstream

* Wed Mar  2 2005 Tomas Mraz <tmraz@redhat.com> - 2.8.2-2
- Rebuild with openssl-0.9.7e

* Wed Jan 26 2005 Matthias Clasen <mclasen@redhat.com> - 2.8.2-1
- Update to 2.8.2

* Wed Nov 24 2004 Owen Taylor <otaylor@redhat.com> - 2.8.0-4
- Fix problem with Lain glyphs when subsetting some Asian fonts (#140010)

* Thu Sep 30 2004 Matthias Clasen <mclasen@redhat.com> - 2.8.0-2
- Fix display of queue length in the print dialog

* Mon Sep 27 2004 Owen Taylor <otaylor@redhat.com> - 2.8.0-1
- Version 2.8.0

* Fri Sep 03 2004 Matthias Clasen <mclasen@redhat.com> - 2.7.1-7
- Make updating the printer list async.

* Tue Aug 31 2004 Matthias Clasen <mclasen@redhat.com> - 2.7.1-6
- Update the async ppd patch

* Sat Aug 28 2004 Colin Walters <walters@redhat.com> - 2.7.1-5
- Do not actually apply session printing patch yet, need to
  wait for eggcups to support it.

* Fri Aug 27 2004 Matthias Clasen <mclasen@redhat.com> - 2.7.1-4
- Update and apply async ppd patch

* Fri Aug 13 2004 Colin Walters <walters@redhat.com> - 2.7.1-3
- Add session printing patch

* Wed Aug 11 2004 David Malcolm <dmalcolm@redhat.com> - 2.7.1-2
- Added explicit Pango dependency (1.5 or better) to fix problem with missing symbols (#129518)

* Tue Aug  3 2004 Owen Taylor <otaylor@redhat.com> - 2.7.1-1
- Upgrade to 2.7.1
- BuildRequires zlib-devel and intltooll (#111106, Maxim Dzumanenko)

* Fri Jul 30 2004 Colin Walters <walters@redhat.com> 2.7.0-4
- Add patch to remove polling of printer queues
- BuildRequire latest libgnomecups

* Thu Jul 29 2004 Colin Walters <walters@redhat.com> 2.7.0-3
- Backport patch to fix crash when no printers are available
- Require pango 1.4

* Thu Jun 17 2004 Matthias Clasen <mclasen@redhat.com> 2.7.0-2
- Add Location information to the gpa printer state.

* Tue Jun 15 2004 Colin Walters <walters@redhat.com> 2.7.0-1
- Update to 2.7.0 CVS
- Add current version of patch which implements dynamic updating,
  using libgnomecups.
- Add Requires: libgnomecups. 
- Add BuildPrereq: libgnomecups-devel. 

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Apr  1 2004 Alex Larsson <alexl@redhat.com> 2.6.0-1
- update to 2.6.0

* Tue Mar 16 2004 Mike A. Harris <mharris@redhat.com> 2.5.4-2
- Removed PreReq: XFree86, as it seems bogus.  Probably a leftover from a
  long time ago that is not needed anymore.  This change is needed in order
  to make the package X11 implementation agnostic, however if there is
  something that it does really require from the XFree86 package, we can
  use a file or directory dependancy instead, or a virtual provide can be
  added if need be.
- Added Requires(post): /sbin/ldconfig
- Added Requires(postun): /sbin/ldconfig

* Fri Mar 12 2004 Alex Larsson <alexl@redhat.com> 2.5.4-1
- update to 2.5.4

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 26 2004 Alexander Larsson <alexl@redhat.com> 2.5.3-1
- update to 2.5.3

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 28 2004 Alexander Larsson <alexl@redhat.com> 2.5.1-1
- update to 2.5.1

* Wed Jan  7 2004 Owen Taylor <otaylor@redhat.com> 2.4.2-1.1
- Upgrade to 2.4.2

* Thu Oct 23 2003 Owen Taylor <otaylor@redhat.com> 2.4.0-1
- Upgrade to 2.4.0

* Thu Aug 28 2003 Owen Taylor <otaylor@redhat.com> 2.3.1-2
- Make the fallback font "Sans Regular", not "Helvetica". Helvetica 
  was ending up picking the alphabetically first font on the system.
  (#79271. Tim Waugh)

* Tue Aug 19 2003 Alexander Larsson <alexl@redhat.com> 2.3.1-1
- update for gnome 2.3

* Fri Aug  1 2003 Bill Nottingham <notting@redhat.com> 2.2.1.3-4
- remove extraneous libxml dependency

* Wed Jul  9 2003 Owen Taylor <otaylor@redhat.com> 2.2.1.3-3.0
- Bump for rebuild

* Mon Jun 23 2003 Owen Taylor <otaylor@redhat.com> 2.2.1.3-2
- Add --add-missing to automake

* Mon Jun 23 2003 Owen Taylor <otaylor@redhat.com> 2.2.1.3-1
- Version 2.2.1.3

* Thu Jun 12 2003 Owen Taylor <otaylor@redhat.com> 2.2.1.2-2
- Version 2.2.1.2
- Fix problem with mismatched libtool

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 24 2003 Owen Taylor <otaylor@redhat.com>
- Fix crash from HP Color LaserJet 4500 PPD file 
  (http://bugzilla.gnome.org/show_bug.cgi?id=106984)

* Fri Feb 14 2003 Tim Powers <timp@redhat.com> 2.2.1.1-2
- remove buildreq on Xft

* Tue Feb  4 2003 Alexander Larsson <alexl@redhat.com> 2.2.1.1-1
- Update to 2.2.1.1 (needed for new gedit)

* Tue Jan 28 2003 Matt Wilson <msw@redhat.com> 2.1.8-4
- BuildPrereq: cups-devel and use LIBTOOL=/usr/bin/libtool

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 17 2003 Havoc Pennington <hp@redhat.com>
- rebuild to get all arches

* Thu Jan 16 2003 Havoc Pennington <hp@redhat.com>
- 2.1.8

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 2.1.4-3
- rebuild

* Mon Dec 16 2002 Havoc Pennington <hp@redhat.com>
- initial build of libgnomeprint 2.2 (version 2.1.4)
- don't try to prereq ourselves, wtf was that about

