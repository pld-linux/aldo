Summary:	Morse code tutor
Summary(pl.UTF-8):	Program do nauki alfabetu Morse'a
Name:		aldo
Version:	0.7.5
Release:	1
License:	GPL
Group:		Applications
Source0:	http://savannah.nongnu.org/download/aldo/%{name}-%{version}.tar.bz2
# Source0-md5:	385eaec5a6d293195aa5fa6a00b1cfcf
URL:		http://www.nongnu.org/aldo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libao-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALDO is a morse tutor with 6 skill levels and 4 speeds. Select the
proper skill/speed to begin practicing cw.

%description -l pl.UTF-8
ALDO to program do nauki alfabetu Morse'a. Posiada 6 poziomów
trudności i 4 prędkości. Wystarczy wybrać odpowiedni poziom i prędkość
aby zacząć ćwiczyć telegrafię.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
