Summary:	The GNU patch command, for modifying/upgrading files
Name:		patch
Version:	2.7.6
Release:	1
License:	GPLv3
Group:		Text tools
Url:		http://www.gnu.org/directory/GNU/patch.html
Source0:	ftp://ftp.gnu.org/gnu/patch/%{name}-%{version}.tar.xz
Patch3:		patch-2.6-stderr.patch
Patch6:		patch-2.6-fix-str-fmt.patch
Patch8:		patch-2.7.1-fix-segfault-in-parsing-of-incorrect-args.patch
# debian patches:
Patch103:	lenny-options.diff
BuildRequires:	attr-devel

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
%apply_patches

%build
%configure
%make

%install
%makeinstall

%files
%doc NEWS README AUTHORS ChangeLog
%{_bindir}/*
%{_mandir}/man1/*
