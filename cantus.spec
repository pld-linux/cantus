%define name cantus
%define version 1.0
%define release 1
%define summary A GUI tool to rename and tag mp3 and ogg/vorbis files

Summary:	%{summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPL
URL:		http://software.manicsadness.com/cantus
Group:		Applications/Multimedia
######		Unknown group!
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gtk+ >= 1.2.3 gnome-libs-devel >= 1.2.8
Requires:	gtk+ >= 1.2.3 gnome-libs >= 1.2.8 libogg libvorbis

%description
cantus is a suite to rename and tag mp3 and ogg/vorbis files. It is
free software, and distributed under the terms of the GPL. It was
written by sam (Samuel Abels, sam@manicsadness.com) and implemented in
C using the GTK.

Features:

- define rules for renaming, which you can proceed on a list of files
- mass renaming/tagging of mp3s
- define rules to apply on a queue of mp3files
- dynamically tagging is implemented, that means, you can generate a
  tag out of the filename and/or directory name
- renaming of files through freedb
- a LOT more

%prep
%setup -q

%build
%{__autoconf}
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc COPYING
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}/*.xpm
