Summary:	gmbCrossword - making crosswords
Summary(pl):	gmbCrossword - tworzenie krzy��wek
Name:		gmbcrossword
Version:	0.7
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gmbcrossword/%{name}-%{version}.tar.gz
# Source0-md5:	f69a7ad1d4a76a6028383aa12f16e108
URL:		http://gmbcrossword.sourceforge.net/
Requires:	gambas-gb-db-sqlite
Requires:	gambas-gb-qt-ext
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gmbCrossword is an application for making Swedish type crosswords. It
is written in Gambas and has support for word lookup in databases.

%description -l pl
gmbCrossword jest aplikacj� s�u��c� do robienia krzy��wek. Zosta�a
napisana w Gambasie i wspiera wyszukiwanie s��w w bazach danych.

%package words
Summary:	gmbCrossword - base wordlists
Summary(pl):	gmbCrossword - podstawowa lista s��w
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description words
In the distribution file you'll find databases for English, Swedish
and computer words. They are rather small databases (10000-20000
words) to keep the filesize down but it is easy to import new words. I
also have a bigger Swedish file (>200000 words) but it is not
currently in the distribution.

%description words -l pl
Tutaj znajduj� si� bazy s��w dla j�zyka angielskiego, szwedzkiego oraz
wyra�e� komputerowych. S� do�� ma�e (10000-20000 s��w), aby utrzyma�
ma�y rozmiar pliku dystrybucyjnego, ale �atwo dodawa� nowe s�owa.
Autor dysponuje wi�kszym plikiem s�ownika szwedzkiego (>200000 s��w),
ale nie jest on aktualnie dystrybuowany.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install gmbcrossword $RPM_BUILD_ROOT%{_bindir}/gmbcrossword
install databases/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README 
%attr(755,root,root) %{_bindir}/gmbcrossword
%dir %{_datadir}/%{name}

%files words
%defattr(644,root,root,755)
%{_datadir}/%{name}/*
