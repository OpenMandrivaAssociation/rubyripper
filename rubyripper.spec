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
Requires:   rubygem(gettext)
# for cd-discid
Requires:   abcde
Requires:   vorbis-tools vorbisgain
BuildRequires:  cdparanoia
BuildRequires:  rubygem(gettext)
BuildArch:  noarch

Suggests:   rubyripper-gtk
Suggests:   mp3gain
Suggests:   flac
Suggests:   normalize

%description
Rubyripper is a digital audio extraction algorithm that uses cdparanoia
error correcting power and it's own secure ripping algorithm to make
sure that a CD rip is done successfully and accurately.

%files -f %{name}.lang
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
%find_lang %{name}

%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.2-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Thu Jan 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6.2-1
+ Revision: 762368
- version update 0.6.2

* Sun Aug 01 2010 Rémy Clouard <shikamaru@mandriva.org> 0.6.0-1mdv2011.0
+ Revision: 564482
- New version 0.6.0
- sanitize spec file (remove tabs)
- fix link for Source0
- use the --enable-lang-all option

* Sun Feb 21 2010 Rémy Clouard <shikamaru@mandriva.org> 0.5.7-2mdv2010.1
+ Revision: 508995
- fix build error : when gtk2 is found but display is not available,
  Gtk::Init throws a RuntimeError that make the build fail,
  so we have to catch it

* Sat Sep 19 2009 Rémy Clouard <shikamaru@mandriva.org> 0.5.7-1mdv2010.0
+ Revision: 444654
- new release

* Thu Jun 04 2009 Rémy Clouard <shikamaru@mandriva.org> 0.5.5-3mdv2010.0
+ Revision: 382591
- fix missing require ruby-gettext
- fix lang not being generated (option --enable-lang=all does not work)
- fix various rpmlint warnings
- use configure2_5x

* Sat Apr 11 2009 Pascal Terjan <pterjan@mandriva.org> 0.5.5-2mdv2009.1
+ Revision: 366207
- Don't require libdiscid0 (it doesn't exist on x86_64 and is not used anyway)
  Require abcde instead for cd-discid

* Fri Mar 20 2009 Nicolas Vigier <nvigier@mandriva.com> 0.5.5-1mdv2009.1
+ Revision: 359132
- noarch package
- add cdparanoia BR
- license is GPLv3+
- import rubyripper package from CLOUARD R?\195?\169my (shikamaru) (#47486)


