Summary:	The GNU patch command, for modifying/upgrading files
Name:		patch
Version:	2.8
Release:	1
License:	GPLv3
Group:		Text tools
Url:		https://www.gnu.org/directory/GNU/patch.html
Source0:	https://ftp.gnu.org/pub/gnu/patch/%{name}-%{version}.tar.xz
#Patch1:		patch-2.6-stderr.patch
#Patch2:		patch-2.6-fix-str-fmt.patch
#Patch3:		patch-2.7.6-check-for-__builtin_mul_overflow_p.patch
# debian patches:
#Patch103:	lenny-options.diff
BuildSystem:	autotools
BuildRequires:	attr-devel

%description
The patch program applies diff files to originals.  The diff command
is used to compare an original to a changed file.  Diff lists the
changes made to the file.  A person who has the original file can then
use the patch command with the diff file to add the changes to their
original file (patching the file).

Patch should be installed because it is a common way of upgrading
applications.

%files
%doc NEWS README AUTHORS ChangeLog
%{_bindir}/*
%{_mandir}/man1/*
