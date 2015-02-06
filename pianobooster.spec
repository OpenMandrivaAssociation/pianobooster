Name:            pianobooster
Summary:         A MIDI file player that teaches you how to play the piano
Version:         0.6.4b
Release:         3
License:         GPLv3+
Group:           Sound
URL:             http://pianobooster.sourceforge.net/
Source0:         http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz
Source1:         %{name}.desktop
# link libpthread and libGL explicitly
Patch0:          pianobooster-0.6.4b-explicit-linking.patch
BuildRequires:   cmake
BuildRequires:   qt4-devel
BuildRequires:   desktop-file-utils
BuildRequires:   pkgconfig(alsa)
BuildRequires:   mesaglu-devel

%description
A MIDI file player/game that displays the musical notes AND teaches you how
to play the piano. 

PianoBooster is a fun way of playing along with a musical accompaniment and
at the same time learning the basics of reading musical notation.
The difference between playing along to a CD or a standard MIDI file
is that PianoBooster listens and reacts to what you are playing on a
MIDI keyboard.


%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1 -b .linkpthread
perl -pi -e "s/-mwindows//g" src/CMakeLists.txt

sed -e 's|\r||g' README.txt > README.txt.tmp
touch -r README.txt README.txt.tmp
mv README.txt.tmp README.txt

sed -e 's|\r||g' license.txt > license.txt.tmp
touch -r license.txt license.txt.tmp
mv license.txt.tmp license.txt

find -name '*.cpp' -exec chmod a-x {} \;
find -name '*.h' -exec chmod a-x {} \;

%build
%cmake ../src
make %{?_smp_mflags}

%install
pushd build
install -d %{buildroot}%{_bindir}
install %{name} %{buildroot}%{_bindir}
popd

install -d $%{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications  \
    %{SOURCE1}


install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -m 644 -p src/images/Logo32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -d %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -m 644 -p src/images/logo64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(-,root,root,-)
%doc license.txt gplv3.txt README.txt
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*



%changelog
* Mon Jan 16 2012 Vladimir Testov <vladimir.testov@rosalab.ru> 0.6.4b-1
+ Revision: 761707
- builreq corrected again
- builreq corrected
- builreq added
- fixed group
- Add pianobooster
- Add pianobooster
- Created package structure for pianobooster.

