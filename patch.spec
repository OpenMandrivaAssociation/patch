Summary:	The GNU patch command, for modifying/upgrading files
Name:		patch
Version:	2.6.1
Release:	%mkrel 6
License:	GPLv3
Group:		Text tools
URL:		http://www.gnu.org/directory/GNU/patch.html
Source0:	ftp://ftp.gnu.org/gnu/patch/%{name}-%{version}.tar.bz2
Patch1:		patch-2.6-sigsegv.patch
Patch3:		patch-2.6-stderr.patch
Patch6:		patch-2.6-fix-str-fmt.patch
Patch7:		buildfix.diff
# debian patches:
Patch103:	lenny-options.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The patch program applies diff files to originals.  The diff command
is used to compare an original to a changed file.  Diff lists the
changes made to the file.  A person who has the original file can then
use the patch command with the diff file to add the changes to their
original file (patching the file).

Patch should be installed because it is a common way of upgrading
applications.

%prep
%setup -q

%patch1 -p1 -b .sigsegv
%patch3 -p1 -b .stderr
%patch6 -p0 -b .format_not_a_string_literal_and_no_format_arguments
%patch7 -p0 -b .buildfix
%patch103 -p1 -b .compat-options

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc NEWS README AUTHORS ChangeLog
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/*/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.6.1-5mdv2011.0
+ Revision: 666991
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6.1-4mdv2011.0
+ Revision: 607074
- rebuild

* Wed May 05 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.6.1-3mdv2010.1
+ Revision: 542386
- use %%configure2_5x
- fix source0

* Mon May 03 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.6.1-2mdv2010.1
+ Revision: 541900
- Give a more clean name for a patch
- Fix license according to COPYING file

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 2.6.1-1mdv2010.1
+ Revision: 484251
- update to new version 2.6.1

* Thu Dec 03 2009 Thierry Vignaud <tv@mandriva.org> 2.6-1mdv2010.1
+ Revision: 472899
- new release
- drop patch 2, 5, 100 & 101 (merged upstream)
- rediff patches 1, 3
- patch 7: add compat options for debian patches merged upstream:
  patch contained two patches that would create reject files in unified
  format, and collect all rejects in a single, "global" reject file. These
  patches are now part of patch 2.6.
   * -U or --unified-reject-files  is now  --reject-format=format.
     Additionally, reject files will automatically be in unified format if the
     input patch is in that format.
   * --global-reject-file=file  is now a synonym for  --reject-file=file (-r)
     which has been fixed not to overwrite reject hunks from different files.

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.5.9-9mdv2010.0
+ Revision: 426356
- rebuild

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 2.5.9-8mdv2009.1
+ Revision: 317535
- rediffed one fuzzy patch (P1)
- fix build with -Werror=format-security (P6)

* Tue Oct 28 2008 Pixel <pixel@mandriva.com> 2.5.9-7mdv2009.1
+ Revision: 297998
- cleanup unneeded hacks: remove -D_GNU_SOURCE (added for powerpc in 2000),
  remove --disable-largefile (added for sparcs in 2000)
- add patches from debian implementing --unified-reject-files (great!) and
--global-reject-file=file

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.5.9-6mdv2009.0
+ Revision: 223441
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 2.5.9-5mdv2008.1
+ Revision: 179121
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.5.9-4mdv2007.0
+ Revision: 119966
- Import patch

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.5.9-3mdk
- Rebuild

* Sat Aug 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.5.9-2mdk
- drop useless prefix

