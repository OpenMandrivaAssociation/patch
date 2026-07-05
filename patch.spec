Summary:	The GNU patch command, for modifying/upgrading files
Name:		patch
Version:	2.8
Release:	2
License:	GPLv3
Group:		Text tools
Url:		https://www.gnu.org/directory/GNU/patch.html
Source0:	https://ftp.gnu.org/pub/gnu/patch/%{name}-%{version}.tar.xz
BuildSystem:	autotools
BuildRequires:	attr-devel

%patchlist
patch-gitbinary.patch

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
