Summary:	Morse code tutor
Summary(pl):	Program do nauki alfabetu Morse'a
Name:		aldo
Version:	0.6.3
Release:	2
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	7548bed9282f4581858648236a9ac5e0
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
