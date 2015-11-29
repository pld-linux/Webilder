Summary:	Flickr wallpaper downloader
Name:		Webilder
Version:	0.6.4
Release:	0.1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://www.webilder.org/static/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	54ae36a6e050b7f4fffa7a62f8f2c44b
URL:		http://www.webilder.org/
BuildRequires:	python-devel
BuildRequires:	python-gnome-desktop-applet
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Webilder delivers stunning wallpapers to your Linux desktop, directly from
Flickr and Webshots. You choose what keywords (tags) to watch for, and photos
are automatically downloaded to your computer. Webilder can also change the
wallpaper every few minutes.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bonobo/servers/*.server
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{py_sitescriptdir}/webilder
%{py_sitescriptdir}/Webilder*.egg-info
%{_datadir}/webilder
