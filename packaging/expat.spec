Name:           expat
Version:        2.1.0
Release:        0
Url:            http://expat.sourceforge.net/
Summary:        XML Parser Toolkit
License:        MIT
Group:          Development/Libraries/C and C++
Source0:        %{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Patch2:         expat-visibility.patch
Patch3:         expat-alloc-size.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
Expat is an XML 1.0 parser written in C. It aims to be fully
conformant. It is currently not a validating XML processor. The current
production version of expat can be downloaded from
ftp://ftp.jclark.com/pub/xml/expat.zip. The directory xmltok contains a
low-level library for tokenizing XML. The interface is documented in
xmltok/xmltok.h. The directory xmlparse contains an XML parser library
that is built on top of the xmltok library. The interface is documented
in xmlparse/xmlparse.h. The directory sample contains a simple example
program using this interface. The file sample/build.bat is a batch
file to build the example using Visual C++. The directory xmlwf
contains the xmlwf application, which uses the xmlparse library. The
arguments to xmlwf are one or more files to check for well-formedness.
An option -d dir can be specified. For each well-formed input file, the
corresponding canonical XML is written to dir/f, where f is the
filename (without any path) of the input file. A -x option causes
references to external general entities to be processed. A -s option
makes documents that are not stand-alone cause an error (a document is
considered stand-alone if it is intrinsically stand-alone because it
has no external subset and no references to parameter entities in the
internal subset or it is declared as stand-alone in the XML
declaration).

%package -n libexpat
Summary:        XML Parser Toolkit
Group:          Development/Libraries/C and C++

%description -n libexpat
Expat is an XML 1.0 parser written in C. It aims to be fully
conformant. It is currently not a validating XML processor. The current
production version of expat can be downloaded from
ftp://ftp.jclark.com/pub/xml/expat.zip. The directory xmltok contains a
low-level library for tokenizing XML. The interface is documented in
xmltok/xmltok.h. The directory xmlparse contains an XML parser library
that is built on top of the xmltok library. The interface is documented
in xmlparse/xmlparse.h. The directory sample contains a simple example
program using this interface. The file sample/build.bat is a batch
file to build the example using Visual C++. The directory xmlwf
contains the xmlwf application, which uses the xmlparse library. The
arguments to xmlwf are one or more files to check for well-formedness.
An option -d dir can be specified. For each well-formed input file, the
corresponding canonical XML is written to dir/f, where f is the
filename (without any path) of the input file. A -x option causes
references to external general entities to be processed. A -s option
makes documents that are not stand-alone cause an error (a document is
considered stand-alone if it is intrinsically stand-alone because it
has no external subset and no references to parameter entities in the
internal subset or it is declared as stand-alone in the XML
declaration).

%package -n libexpat-devel
Summary:        XML Parser Toolkit
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libexpat = %{version}
Provides:	expat-devel

%description -n libexpat-devel
Expat is an XML 1.0 parser written in C. It aims to be fully
conformant. It is currently not a validating XML processor. The current
production version of expat can be downloaded from
ftp://ftp.jclark.com/pub/xml/expat.zip. The directory xmltok contains a
low-level library for tokenizing XML. The interface is documented in
xmltok/xmltok.h. The directory xmlparse contains an XML parser library
that is built on top of the xmltok library. The interface is documented
in xmlparse/xmlparse.h. The directory sample contains a simple example
program using this interface. The file sample/build.bat is a batch
file to build the example using Visual C++. The directory xmlwf
contains the xmlwf application, which uses the xmlparse library. The
arguments to xmlwf are one or more files to check for well-formedness.
An option -d dir can be specified. For each well-formed input file, the
corresponding canonical XML is written to dir/f, where f is the
filename (without any path) of the input file. A -x option causes
references to external general entities to be processed. A -s option
makes documents that are not stand-alone cause an error (a document is
considered stand-alone if it is intrinsically stand-alone because it
has no external subset and no references to parameter entities in the
internal subset or it is declared as stand-alone in the XML
declaration).

%prep
%setup -q 
%patch2 -p1
%patch3
rm -f examples/*.dsp

%build
autoreconf -fi
%configure --disable-static --with-pic
make %{?_smp_mflags}

%check
make check

%install
%make_install
rm doc/xmlwf.1

%post -n libexpat -p /sbin/ldconfig

%postun -n libexpat -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc COPYING 
%doc %{_mandir}/man?/*
%{_bindir}/xmlwf

%files -n libexpat
%defattr(-, root, root)
%{_libdir}/libexpat.so.*

%files -n libexpat-devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/libexpat.so
%{_libdir}/pkgconfig/expat.pc

%changelog