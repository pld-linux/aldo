Summary:	Morse code tutor
Summary(pl):	Program do nauki alfabetu Morse'a
Name:		aldo
Version:	0.0.12
Release:	2
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
#Source0-MD5:	e0c793915e131f34ea7a7a94a173350e
Patch0:		%{name}-DESTDIR.patch
URL:		http://aldo.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALDO is a morse tutor with 6 skill levels and 4 speeds.
Select the proper skill/speed to begin practicing cw.

%description -l pl
ALDO to program do nauki alfabetu Morse'a. Posiada 6 
poziomów trudno¶ci i 4 prêdko¶ci. Wybierz odpowiedni poziom i
prêdko¶æ by zacz±æ æwiczyæ telegrafiê.
 
%prep
%setup -q -n %{name}.%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
