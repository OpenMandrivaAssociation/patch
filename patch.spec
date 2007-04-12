Summary:	The GNU patch command, for modifying/upgrading files
Name:		patch
Version:	2.5.9
Release:	%mkrel 4
License:	GPL
Group:		Text tools
URL:		http://www.gnu.org/directory/GNU/patch.html
Source:		ftp://alpha.gnu.org/gnu/patch/%{name}-%{version}.tar.bz2
Patch1:		patch-2.5.8-sigsegv.patch
Patch2:		patch-2.5.4-unreadable_to_readable.patch
Patch3:		patch-2.5.8-stderr.patch
Patch5:		patch-2.5.4-destdir.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1

%build
# (fg) Large file support can be disabled from ./configure - it is necessary at
# least on sparcs
%ifnarch sparc sparc64 alpha
%configure 
%else
%configure --disable-largefile
%endif

make "CFLAGS=%{optflags} -D_GNU_SOURCE -W -Wall" LDFLAGS=-s


%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc NEWS README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*


