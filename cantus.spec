Summary:	A GUI tool to rename and tag mp3 and ogg/vorbis files
Summary(pl):	Graficzne narz�dzie do zmiany nazw i znacznik�w plik�w mp3 i ogg/vorbis
Name:		cantus
Version:	1.04
Release:	1
Group:		X11/Applications/Multimedia
# http://software.manicsadness.com/dlcounter.php?id=16&file=%{name}-%{version}-1.tar.gz
Source0:	%{name}-%{version}-1.tar.gz
License:	GPL
URL:		http://software.manicsadness.com/cantus/
BuildRequires:	autoconf
BuildRequires:	gnome-libs-devel >= 1.2.8
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
Requires:	gnome-libs >= 1.2.8
Requires:	gtk+ >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cantus is a suite to rename and tag mp3 and ogg/vorbis files. It is
free software, and distributed under the terms of the GPL. It was
written by sam (Samuel Abels, <sam@manicsadness.com>) and implemented
in C using the GTK.

Features:
- define rules for renaming, which you can proceed on a list of files
- mass renaming/tagging of mp3s
- define rules to apply on a queue of mp3 files
- dynamically tagging is implemented, that means, you can generate a
  tag out of the filename and/or directory name
- renaming of files through freedb
- a LOT more

%description -l pl
cantus to zestaw narz�dzi do zmiany nazw i znacznik�w plik�w mp3 i
ogg/vorbis. Jest to wolnodost�pne oprogramowanie, rozpowszechaniane
na licencji GPL. Zosta�o napisane przez sama (Samuela Abelsa,
<sam@manicsadness.com>) i zaimplementowany w C przy u�yciu GTK.

Mo�liwo�ci:
- definiowanie regu� zmiany nazw, do wykonania na li�cie plik�w
- masowa zmiana nazw i znakowanie plik�w mp3
- definiowanie regu� do wykonania na kolejce plik�w mp3
- zaimplementowane dynamiczne znakowanie, co oznacza, �e mo�na
  generowa� znaczniki na podstawie nazwy pliku i/lub katalogu
- zmiana nazw plik�w poprzez freedb
- WIELE wi�cej.

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

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