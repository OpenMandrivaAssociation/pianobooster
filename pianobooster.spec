%define orig_name PianoBooster

Name:           pianobooster
Version:        0.7.2b
Release:        1
Summary:        A MIDI file player that teaches you how to play the piano
Group:          Sound/Midi
License:        GPLv3+
Url:            https://github.com/captnfab/PianoBooster
Source0:        https://github.com/captnfab/PianoBooster/archive/v%{version}/%{orig_name}-%{version}.tar.gz


BuildRequires:  cmake
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
BuildRequires:  hicolor-icon-theme

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
%{_datadir}/games/%{name}/translations/music*.qm
%{_datadir}/games/%{name}/translations/*.json
%{_mandir}/man6/%{name}.6*

#----------------------------------------------------------------------------
%if 0
# Changed USE_FLUIDSYNTH to EXPERIMENTAL_USE_FLUIDSYNTH as this option is not working yet

%package        fluidsynth
Summary:        Wrapper to launch PianoBooster with FluidSynth as MIDI sequencer
Group:          Sound/Midi
BuildRequires:  pkgconfig(fluidsynth)
Requires:       %{name} = %{version}-%{release}
Requires:       fluidsynth
Requires:       fluid-soundfont-gm
Requires:       fluid-soundfont-gs
Requires:       libnotify

%description    fluidsynth
This package contains a wrapper script to launch PianoBooster together with
FluidSynth in ALSA server mode. This makes it possible to play the MIDI files
even without a plugged-in MIDI keyboard.

%files          fluidsynth
%{_gamesbindir}/%{name}-fluidsynth
%{_datadir}/applications/%{name}-fluidsynth.desktop
%endif
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
       -DEXPERIMENTAL_USE_FLUIDSYNTH=OFF \
       -DWITH_MAN=ON
%make_build

#Qmake is alternative options to build. Use if cmake fail.
#%qmake_qt5 \
#       USE_SYSTEM_FONT=ON \
#       NO_DOCS=ON \
#       NO_LICENSE=ON \
#       NO_CHANGELOG=ON \
#       INSTALL_ALL_LANGS=ON \
#       USE_BUNDLED_RTMIDI=OFF \
#       EXPERIMENTAL_USE_FLUIDSYNTH=OFF \
#       WITH_MAN=ON


%install

%make_install

