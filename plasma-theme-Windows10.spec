Name: plasma-theme-Windows10
Summary: Plasma theme resembling Windows 10
Version: 1.0
Release: 4
Url: https://store.kde.org/p/998654/
Source0: https://dllb2.pling.com/api/files/download/id/1523535246/s/f226e1b71312610e9d253f181f67267489e20a671e6dc425930ddcc900baf52ba2843457f7f2dddd91a1406231fe0eb724fcd850189d5ada3c941000093d7f7f/t/1578949153/c/f226e1b71312610e9d253f181f67267489e20a671e6dc425930ddcc900baf52ba2843457f7f2dddd91a1406231fe0eb724fcd850189d5ada3c941000093d7f7f/lt/download/windows_10_plasma_theme.zip
Source1: https://github.com/B00merang-Project/Windows-10/releases/download/v0.9.9-AU/Windows.10.Icons.v0.5.tar.gz
# https://store.kde.org/p/1172409/
Source2: https://dllb2.pling.com/api/files/download/id/1559572296/s/6c32e2ff9eb1db603f83e14474484d8c68b7889f059b97f65cd96fb12089f2c9613e17aeee312dfc4ce1b74ef5174c0d1485007080e55fdfd3e0bb5f8dc5cfac/t/1578950709/c/f226e1b71312610e9d253f181f67267489e20a671e6dc425930ddcc900baf52ba2843457f7f2dddd91a1406231fe0eb724fcd850189d5ada3c941000093d7f7f/lt/download/WindowsK10(0.6.2).tar.gz
Source3: https://github.com/Infinality/mouse-cursors/raw/master/aero-drop.tar.gz
Group: Graphical Desktop/KDE
License: GPLv3
BuildArch: noarch
BuildRequires: distro-release-theme

%description
Plasma theme resembling Windows 10.

%prep
# Nothing to do...

%build
# Nothing to do...

%install
mkdir -p %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}/plasma/desktoptheme %{buildroot}%{_datadir}/aurorae/themes
cd %{buildroot}%{_datadir}/plasma/desktoptheme
tar xf "%{S:0}"
mv "Windows 10 Plasma Theme" Windows10
cd %{buildroot}%{_datadir}/icons
tar xf "%{S:1}"
mv "Windows 10 Icons" Windows10
# Get rid of Linux Mint logo...
cp -f %{_datadir}/icons/hicolor/scalable/apps/openmandriva.svg Windows10/scalable/places/start-here.svg
cd %{buildroot}%{_datadir}/aurorae/themes
tar xf "%{S:2}"
cd %{buildroot}%{_datadir}/icons
tar xf "%{S:3}"
mv aero-drop/cursors Windows10/
mv aero-drop/index.theme Windows10/cursor.theme
rmdir aero-drop
cd %{buildroot}
find . -type d |xargs chmod 0755
find . -type f |xargs chmod 0644

%files
%{_datadir}/icons/Windows10
%{_datadir}/plasma/desktoptheme/Windows10
%{_datadir}/aurorae/themes/*
