Summary:	A GUI tool to rename and tag mp3 and ogg/vorbis files
Summary(pl):	Graficzne narzêdzie do zmiany nazw i znaczników plików mp3 i ogg/vorbis
Name:		cantus
Version:	1.07
Release:	1
License:	GPL
Group:		X11/Applications/Sound
# http://software.manicsadness.com/dlcounter.php?id=16&file=%{name}-%{version}-1.tar.gz
Source0:	http://sam.homeunix.com/software.manicsadness.com-step4/releases/cantus/%{name}-%{version}-1.tar.gz
# Source0-md5:	0e1ec373ac87a1b7ca604d055548b92b
URL:		http://software.manicsadness.com/cantus/
BuildRequires:	autoconf
BuildRequires:	gnome-libs-devel >= 1.2.8
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
Requires:	gnome-libs >= 1.2.8
Requires:	gtk+ >= 1.2.3
Obsoletes:	gmp3
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
cantus to zestaw narzêdzi do zmiany nazw i znaczników plików mp3 i
ogg/vorbis. Jest to wolnodostêpne oprogramowanie, rozpowszechniane
na licencji GPL. Zosta³o napisane przez sama (Samuela Abelsa,
<sam@manicsadness.com>) i zaimplementowany w C przy u¿yciu GTK.

Mo¿liwo¶ci:
- definiowanie regu³ zmiany nazw, do wykonania na li¶cie plików
- masowa zmiana nazw i znakowanie plików mp3
- definiowanie regu³ do wykonania na kolejce plików mp3
- zaimplementowane dynamiczne znakowanie, co oznacza, ¿e mo¿na
  generowaæ znaczniki na podstawie nazwy pliku i/lub katalogu
- zmiana nazw plików poprzez freedb
- WIELE wiêcej.

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall \
	gnomemenudir=$RPM_BUILD_ROOT%{_applnkdir}/Utilities

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}/*.xpm
%{_pixmapsdir}/%{name}/*.png
%{_applnkdir}/Utilities/cantus.desktop
