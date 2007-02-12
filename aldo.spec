Summary:	Morse code tutor
Summary(pl.UTF-8):   Program do nauki alfabetu Morse'a
Name:		aldo
Version:	0.6.3
Release:	2
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/aldo/%{name}-%{version}.tar.bz2
# Source0-md5:	7548bed9282f4581858648236a9ac5e0
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.nongnu.org/aldo/
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
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
