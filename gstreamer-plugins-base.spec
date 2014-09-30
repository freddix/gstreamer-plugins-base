%include        /usr/lib/rpm/macros.gstreamer

%define		gstname		gst-plugins-base
%define		gst_major_ver	1.0
%define		gst_req_ver	1.4.3

Summary:	GStreamer Streaming-media framework base plugins
Name:		gstreamer-plugins-base
Version:	1.4.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-base/%{gstname}-%{version}.tar.xz
# Source0-md5:	d8facf3be279585f3ad2e764540376f7
Patch0:		%{name}-default-cd-speed.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	orc-devel >= 0.4.5
BuildRequires:	pkg-config
#
BuildRequires:	alsa-lib-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	freetype-devel
BuildRequires:	libogg-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvisual-devel
BuildRequires:	libvorbis-devel
BuildRequires:	rpm-gstreamerprov
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXv-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gstreamer >= %{gst_req_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}
%define		gstincludedir	%{_includedir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%package libs
Summary:	Gstreamer base plugins - shared libraries
Group:		Libraries

%description libs
Gstreamer base plugins - shared libraries.

%package devel
Summary:	Include files for GStreamer streaming-media framework plugins
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gstreamer-devel >= %{gst_req_ver}

%description devel
Include files for GStreamer streaming-media framework plugins.

%package apidocs
Summary:	GStreamer plugins API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GStreamer plugins API documentation.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1

%build
%{__autopoint}
patch -p0 < common/gettext.patch
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-examples	\
	--disable-silent-rules	\
	--disable-static	\
	--enable-experimental	\
	--with-html-dir=%{_gtkdocdir}		    \
	--with-package-name="GStreamer (Freddix)"   \
	--with-package-origin="http://freddix.org/"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{gstlibdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_bindir}/gst-discoverer-*
%attr(755,root,root) %{_bindir}/gst-play-1.0
%attr(755,root,root) %{_bindir}/gst-device-monitor-1.0

%attr(755,root,root) %{gstlibdir}/libgstadder.so
%attr(755,root,root) %{gstlibdir}/libgstalsa.so
%attr(755,root,root) %{gstlibdir}/libgstapp.so
%attr(755,root,root) %{gstlibdir}/libgstaudioconvert.so
%attr(755,root,root) %{gstlibdir}/libgstaudiorate.so
%attr(755,root,root) %{gstlibdir}/libgstaudioresample.so
%attr(755,root,root) %{gstlibdir}/libgstaudiotestsrc.so
%attr(755,root,root) %{gstlibdir}/libgstcdparanoia.so
%attr(755,root,root) %{gstlibdir}/libgstencodebin.so
%attr(755,root,root) %{gstlibdir}/libgstgio.so
%attr(755,root,root) %{gstlibdir}/libgstlibvisual.so
%attr(755,root,root) %{gstlibdir}/libgstogg.so
%attr(755,root,root) %{gstlibdir}/libgstpango.so
%attr(755,root,root) %{gstlibdir}/libgstplayback.so
%attr(755,root,root) %{gstlibdir}/libgstsubparse.so
%attr(755,root,root) %{gstlibdir}/libgsttcp.so
%attr(755,root,root) %{gstlibdir}/libgsttheora.so
%attr(755,root,root) %{gstlibdir}/libgsttypefindfunctions.so
%attr(755,root,root) %{gstlibdir}/libgstvideoconvert.so
%attr(755,root,root) %{gstlibdir}/libgstvideorate.so
%attr(755,root,root) %{gstlibdir}/libgstvideoscale.so
%attr(755,root,root) %{gstlibdir}/libgstvideotestsrc.so
%attr(755,root,root) %{gstlibdir}/libgstvolume.so
%attr(755,root,root) %{gstlibdir}/libgstvorbis.so
%attr(755,root,root) %{gstlibdir}/libgstximagesink.so
%attr(755,root,root) %{gstlibdir}/libgstxvimagesink.so
%{_mandir}/man1/gst-device-monitor-1.*
%{_mandir}/man1/gst-discoverer-*.1*
%{_mandir}/man1/gst-play-*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*-%{gst_major_ver}.so.?
%attr(755,root,root) %{_libdir}/lib*-%{gst_major_ver}.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*-%{gst_major_ver}.so
%{gstincludedir}/gst/allocators
%{gstincludedir}/gst/app
%{gstincludedir}/gst/audio
%{gstincludedir}/gst/fft
%{gstincludedir}/gst/pbutils
%{gstincludedir}/gst/riff
%{gstincludedir}/gst/rtp
%{gstincludedir}/gst/rtsp
%{gstincludedir}/gst/sdp
%{gstincludedir}/gst/tag
%{gstincludedir}/gst/video
%{_pkgconfigdir}/gstreamer-allocators-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-app-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-audio-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-fft-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-pbutils-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-plugins-base-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-riff-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-rtp-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-rtsp-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-sdp-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-tag-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-video-%{gst_major_ver}.pc
%{_datadir}/gir-1.0/*.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gst-plugins-base-libs-%{gst_major_ver}
%{_gtkdocdir}/gst-plugins-base-plugins-%{gst_major_ver}

