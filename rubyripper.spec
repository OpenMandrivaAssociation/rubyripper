Name:		rubyripper
Summary:	A high precision cd ripper
Version:	0.5.7
Release:	%mkrel 1
Url:		http://code.google.com/p/rubyripper/
License:	GPLv3+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Source0:	%{name}-%{version}.tar.bz2
Requires:	cdparanoia
Requires:	ruby
Requires:	ruby-gettext
# for cd-discid
Requires:	abcde
Requires:	vorbis-tools vorbisgain
BuildRequires:	cdparanoia
BuildRequires:	ruby-gettext
BuildArch:	noarch

Suggests:	rubyripper-gtk
Suggests:	mp3gain
Suggests:	flac
Suggests:	normalize

%description
Rubyripper is a digital audio extraction algorithm that uses cdparanoia
error correcting power and it's own secure ripping algorithm to make
sure that a CD rip is done successfully and accurately.

%files -f %{name}.lang
%defattr(-,root,root)
%_bindir/rrip_cli
%{ruby_sitelibdir}/rr_lib.rb
%doc README


#--------------------------------------------------------------------
%package -n rubyripper-gtk
Summary:	GTK frontend for rubyripper
Group:		Graphical desktop/GNOME
Requires:	rubyripper
Requires:	ruby-gtk2

%description -n rubyripper-gtk
GTK2 frontend for rubyripper

%files -n rubyripper-gtk
%defattr(-,root,root)
%_bindir/rrip_gui
%_iconsdir/hicolor/*/apps/%{name}.png
%_datadir/applications/%{name}.desktop

#--------------------------------------------------------------------
%prep
%setup -q

#specify bindir to avoid binaries to be in /usr/usr/bin
%configure2_5x \
--enable-lang=nl,de,fr,hu,ru,es,se \
--enable-cli \
--enable-gtk2 \
--bindir=/bin 

%install
rm -fr %buildroot
%makeinstall_std

%find_lang %{name}
chmod -x README

%clean
rm -rf %buildroot

