%define oname PianoBooster
%define gitdate 20230122

Summary:	A MIDI file player that teaches you how to play the piano
Name:	pianobooster
Version:	1.0.0
Release:	5
License:	GPLv3+
Group:	Sound/Midi
Url:	https://github.com/captnfab/PianoBooster
# Use git HEAD to pick up Qt6 support
#Source0:	https://github.com/captnfab/PianoBooster/archive/v%%{version}/%%{oname}-%%{version}.tar.gz
Source0:	%{name}-%{gitdate}.tar.xz
BuildRequires:	cmake
BuildRequires:	hicolor-icon-theme
BuildRequires:	qmake-qt6
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(ftgl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Core5Compat)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Help)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6OpenGLWidgets)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	pkgconfig(rtmidi)
Requires:	fonts-ttf-dejavu
Requires:	hicolor-icon-theme
Requires:	unzip
Recommends:	qt6-qttranslations

%description
A MIDI file player/game that displays the musical notes AND teaches you how
to play the piano. It is a fun way of playing along with a musical
accompaniment and at the same time learning the basics of reading musical
notation. The difference between playing along to a CD or a standard MIDI file
is that PianoBooster listens and reacts to what you are playing on a MIDI
keyboard.
To run Piano Booster you need a MIDI Piano Keyboard and a MIDI interface
for the PC. If you don't have a MIDI keyboard you can still try out
PianoBooster, using the PC keyboard ('x' is middle C), but a MIDI piano
is really recommended.

%files
%license license.txt
%doc README.md Changelog.txt doc/faq.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/music
%dir %{_datadir}/games/%{name}/translations
%{_datadir}/games/%{name}/music/*.zip
%{_datadir}/games/%{name}/translations/%{name}*.qm
%{_datadir}/games/%{name}/translations/*.json
%{_mandir}/man6/%{name}.6*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{gitdate}


%build
%cmake \
	-DCMAKE_INSTALL_BINDIR=%{_bindir} \
	-DQT_PACKAGE_NAME=Qt6 \
	-DUSE_SYSTEM_FONT=ON \
	-DNO_DOCS=ON \
	-DNO_LICENSE=ON \
	-DNO_CHANGELOG=ON \
	-DINSTALL_ALL_LANGS=ON \
	-DUSE_BUNDLED_RTMIDI=OFF \
	-DWITH_INTERNAL_FLUIDSYNTH=ON \
	-DWITH_MAN=ON

%make_build


%install
%make_install -C build

