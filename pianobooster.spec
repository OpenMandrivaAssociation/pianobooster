%define orig_name PianoBooster

Name:           pianobooster
Version:        1.0.0
Release:        1
Summary:        A MIDI file player that teaches you how to play the piano
Group:          Sound/Midi
License:        GPLv3+
Url:            https://github.com/captnfab/PianoBooster
Source0:        https://github.com/captnfab/PianoBooster/archive/v%{version}/%{orig_name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  qmake5
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(rtmidi)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(fluidsynth)

Requires:       fonts-ttf-dejavu
Requires:       unzip
Requires:       hicolor-icon-theme

Recommends:     qttranslations5

%description
A MIDI file player/game that displays the musical notes AND teaches you how
to play the piano.

PianoBooster is a fun way of playing along with a musical accompaniment and
at the same time learning the basics of reading musical notation.
The difference between playing along to a CD or a standard MIDI file
is that PianoBooster listens and reacts to what you are playing on a
MIDI keyboard.

To run Piano Booster you need a MIDI Piano Keyboard and a MIDI interface
for the PC. If you don't have a MIDI keyboard you can still try out
PianoBooster, using the PC keyboard ('x' is middle C), but a MIDI piano
is really recommended.

%files
%doc README.md Changelog.txt doc/faq.md
%license license.txt
%{_gamesbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/music
%dir %{_datadir}/games/%{name}/translations
%{_datadir}/games/%{name}/music/*.zip
%{_datadir}/games/%{name}/translations/%{name}*.qm
#{_datadir}/games/%{name}/translations/music*.qm
%{_datadir}/games/%{name}/translations/*.json
%{_mandir}/man6/%{name}.6*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{orig_name}-%{version}

%build
%cmake \
       -DCMAKE_INSTALL_BINDIR=%{_gamesbindir} \
       -DUSE_SYSTEM_FONT=ON \
       -DNO_DOCS=ON \
       -DNO_LICENSE=ON \
       -DNO_CHANGELOG=ON \
       -DINSTALL_ALL_LANGS=ON \
       -DUSE_BUNDLED_RTMIDI=OFF \
       -DEXPERIMENTAL_USE_FLUIDSYNTH=ON \
       -DWITH_MAN=ON
%make_build


%install
%make_install -C build

