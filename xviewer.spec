Name:           xviewer
Version:        2.4.0
Release:        1
Summary:        Fast and functional graphics viewer
License:        GPLv2+ and LGPLv2+
Group:          Graphics/Viewers
Url:            https://github.com/linuxmint/xviewer
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gnome-common
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(cinnamon-desktop)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  shared-mime-info
BuildRequires:  itstool
BuildRequires:  intltool

Recommends:       %{name}-plugins

%description
xviewer is a simple graphics viewer for the Cinnamon desktop and
others which uses the gdk-pixbuf library. It can deal with large
images, and zoom and scroll with constant memory usage. Its goals
are simplicity and standards compliance.

%package devel
Summary:        Fast and functional graphics viewer development files
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description devel
xviewer is a simple graphics viewer for the Cinnamon desktop and
others which uses the gdk-pixbuf library. It can deal with large
images, and zoom and scroll with constant memory usage. Its goals
are simplicity and standards compliance.

%prep
%setup -q
%autopatch -p1

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure2_5x \
  --libexecdir=%{_libexecdir}/%{name}
%make_build

%install
%make_install
%find_lang %{name} --with-gnome
find %{buildroot} -type f -name "*.la" -delete -print

if [ -d %{buildroot}%{_datadir}/GConf/ ]; then
    rm -rf %{buildroot}%{_datadir}/GConf/
fi


%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/help/C/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%files devel
%{_includedir}/%{name}-3.0/
%{_libdir}/pkgconfig/%{name}.pc
