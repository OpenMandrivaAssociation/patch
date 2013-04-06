Summary:	The GNU patch command, for modifying/upgrading files
Name:		patch
Version:	2.7.1
Release:	2
License:	GPLv3
Group:		Text tools
URL:		http://www.gnu.org/directory/GNU/patch.html
Source0:	ftp://ftp.gnu.org/gnu/patch/%{name}-%{version}.tar.xz
Source1:	ftp://ftp.gnu.org/gnu/patch/%{name}-%{version}.tar.xz.sig
Patch1:		patch-2.7-sigsegv.patch
Patch3:		patch-2.6-stderr.patch
Patch6:		patch-2.6-fix-str-fmt.patch
Patch7:		patch-remove-empty-dir.patch
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

%patch1 -p1 -b .sigsegv
%patch3 -p1 -b .stderr
%patch6 -p0 -b .format_not_a_string_literal_and_no_format_arguments
%patch7 -p1 -b .emptydir~
%patch103 -p1 -b .compat-options

%build
%configure2_5x
%make

%install
%makeinstall

%files
%doc NEWS README AUTHORS ChangeLog
%{_bindir}/*
%{_mandir}/*/*
