Name:           libav
Version:        11.1
Release:        2.affectiva%{?dist}
Summary:        Libav video encoding and decoding library
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://libav.org
Source:         %{name}-%{version}.tar.gz
License:        LGPL-2.0+

BuildRequires:	opus-devel
BuildRequires:	x264-devel
BuildRequires:	libvpx-devel

%description
Libav is a complete, cross-platform solution to decode, encode, record, convert and stream audio and video.

%package devel
Summary:        Development headers and libraries for libav
Group:          Productivity/Multimedia
Requires:       %{name} = %{version}
Requires:       bzip2-devel
Requires:	opus-devel
Requires:	x264-devel
Requires:	libvpx-devel

%description devel
Libav is a complete, cross-platform solution to decode, encode, record, convert and stream audio and video.

%package tools
Summary:        Libav tools package
Group:          Productivity/Multimedia
Requires:       %{name} = %{version}

%description tools
Libav is a complete, cross-platform solution to decode, encode, record, convert and stream audio and video.

%prep
%setup -q
./configure --prefix=/usr --bindir=/usr/bin --datadir=/usr/share/avconv --libdir=/usr/lib64 --shlibdir=/usr/lib64 --mandir=/usr/share/man \
 --enable-shared --enable-gpl --enable-libvpx --enable-libx264 --enable-libopus

%build
make %{?jobs:-j%jobs}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/avconv/*.avpreset
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/libavcodec/*.h
%{_includedir}/libavfilter/*.h
%{_includedir}/libavformat/*.h
%{_includedir}/libavutil/*.h
%{_includedir}/libswscale/*.h
%{_includedir}/libavresample/*.h
%{_includedir}/libavdevice/*.h
%{_libdir}/pkgconfig/*.pc

%files tools
%defattr(-,root,root)
%{_bindir}/avprobe
%{_bindir}/avconv
%{_mandir}/man1/avprobe.1*
%{_mandir}/man1/avconv.1*
