#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	gmbCrossword - making crosswords
Summary(pl):	gmbCrossword - tworzenie krzy¿ówek
Name:		gmbcrossword
Version:	0.7
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		X11/Applications
#Icon:		-
Source0:	http://dl.sourceforge.net/gmbcrossword/%{name}-%{version}.tar.gz
# Source0-md5:	f69a7ad1d4a76a6028383aa12f16e108
URL:		http://gmbcrossword.sourceforge.net
Requires:	gambas-gb-qt-ext
Requires:	gambas-gb-db-sqlite
BuildArch:	noarch
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gmbCrossword is an application for making swedish typ crosswords. It is written in Gambas and has support for word lookup in databases. 

%description -l pl
gmbCrossword jest aplikacj± s³u¿±c± do robienia krzy¿ówek. Zosta³a napisana w Gambas i wspiera wyszukiwanie s³ów w bazach danych.

%package words
Summary:	gmbCrossword - base wordlists
Summary(pl):	gmbCrossword - podstawowa lista s³ów
Group:		X11/Applications

%description words
In the distribution file you'll find databases for english, swedish and computer words. They are rather small databases (10000-20000 words) to keep the filesize down but it is easy to import new words. I also have a bigger swedish file (>200000 words) but it is not currently in the distribution.

%description words -l pl
Tutaj znajduj± siê bazy s³ów dla angielskiego, szweckiego oraz wyra¿eñ komputerowych. 

%prep
%setup -q -c %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/usr/bin/,%{_datadir}/%{name}}
install gmbcrossword $RPM_BUILD_ROOT/usr/bin/gmbcrossword
install databases/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README 
%attr(755,root,root) /usr/bin/gmbcrossword

%files words
%defattr(644,root,root,755)
#%doc extras/*.gz
%{_datadir}/%{name}/*
