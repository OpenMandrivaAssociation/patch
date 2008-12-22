Summary:	The GNU patch command, for modifying/upgrading files
Name:		patch
Version:	2.5.9
Release:	%mkrel 8
License:	GPL
Group:		Text tools
URL:		http://www.gnu.org/directory/GNU/patch.html
Source0:	ftp://alpha.gnu.org/gnu/patch/%{name}-%{version}.tar.bz2
Patch1:		patch-2.5.8-sigsegv.patch
Patch2:		patch-2.5.4-unreadable_to_readable.patch
Patch3:		patch-2.5.8-stderr.patch
Patch5:		patch-2.5.4-destdir.patch
Patch6:		patch-2.5.9-format_not_a_string_literal_and_no_format_arguments.diff
# debian patches:
Patch100:	10_unified-reject-files.patch
Patch101:	20_global-reject-file.patch
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
%patch2 -p1 -b .unreadable_to_readable
%patch3 -p1 -b .stderr
%patch5 -p1 -b .destdir
%patch6 -p0 -b .format_not_a_string_literal_and_no_format_arguments

%patch100 -p1 -b .unified-reject-files
%patch101 -p1 -b .global-reject-file

%build
%configure 
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
