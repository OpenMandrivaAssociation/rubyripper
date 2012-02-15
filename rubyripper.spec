Name:       rubyripper
Summary:    A high precision cd ripper
Version:    0.6.2
Release:	2
Url:        http://code.google.com/p/rubyripper/
License:    GPLv3+
Group:      Sound
Source0:    http://rubyripper.googlecode.com/files/%{name}-%{version}.tar.bz2
Patch0:     %{name}-0.5.7-rescue-gtk2.patch
Requires:   cdparanoia
Requires:   ruby
Requires:   ruby-gettext
# for cd-discid
Requires:   abcde
Requires:   vorbis-tools vorbisgain
BuildRequires:  cdparanoia
BuildRequires:  ruby-gettext
BuildArch:  noarch

Suggests:   rubyripper-gtk
Suggests:   mp3gain
Suggests:   flac
Suggests:   normalize

%description
Rubyripper is a digital audio extraction algorithm that uses cdparanoia
error correcting power and it's own secure ripping algorithm to make
sure that a CD rip is done successfully and accurately.

%files
%_bindir/rrip_cli
%{ruby_sitelibdir}/rr_lib.rb
%doc README


#--------------------------------------------------------------------
%package -n rubyripper-gtk
Summary:    GTK frontend for rubyripper
Group:      Graphical desktop/GNOME
Requires:   rubyripper
Requires:   ruby-gtk2

%description -n rubyripper-gtk
GTK2 frontend for rubyripper

%files -n rubyripper-gtk
%_bindir/rrip_gui
%_iconsdir/hicolor/*/apps/%{name}.png
%_datadir/applications/%{name}.desktop

#--------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0

#specify bindir to avoid binaries to be in /usr/usr/bin
%configure2_5x \
--enable-lang-all \
--enable-cli \
--enable-gtk2 \
--bindir=/bin 

%install
%makeinstall_std
chmod -x README
