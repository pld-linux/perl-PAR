# ToDo:
# - include /usr/bin/part and /usr/bin/tkpp or not?
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PAR
Summary:	Perl Archive Toolkit
Summary(pl.UTF-8):	Zestaw narzędzi perlowych do archiwizacji
Name:		perl-PAR
Version:	1.005
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/PAR/%{pdir}-%{version}.tar.gz
# Source0-md5:	a1a7d8cc4deb106c3e04b190fa2d9325
URL:		http://par.perl.org/
BuildRequires:	perl-Archive-Zip >= 1.00
%if %{with tests}
BuildRequires:	perl-Compress-Zlib >= 1.30
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-Module-ScanDeps >= 0.45
BuildRequires:	perl-Module-Signature >= 0.35
%endif
BuildRequires:	perl-PAR-Dist >= 0.06
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Archive Toolkit:
- Do what JAR (Java Archive) does for Perl
- Platform-independent, compressed file format (zip)
- Aggregates modules, scripts and other files into one file
- Easy to generate, update and extract
Benefits of using PAR:
- Reduced download and deployment time
- Saves disk space by compression and selective packaging
- Version consistency: solves forward-compatibility problems
- Community support: par@perl.org
You can also turn a PAR file into a self-contained script
- Bundles all necessary 3rd-party modules with it
- Requires only core Perl to run on the target machine
- If you use pp to compile the script...
- ...you get an executable not even needing core Perl

%description -l pl.UTF-8
Perl Archive Toolkit:
- robi to samo, co JAR (archiwizator Javy), ale dla Perla
- używa niezależnego od platformy, formatu pliku skompresowanego (zip)
- integruje w jeden plik moduły, skrypty i inne pliki
- pliki PAR są łatwe do wygenerowania, aktualizacji i rozpakowania
Korzyści płynące ze stosowania PAR:
- skrócenie czasu pobierania i wdrożenia programu
- oszczędność miejsca na dysku wynikająca z kompresji i wybiórczego
  pakietowania
- spójność wersji: rozwiązuje problemy zgodności w przód
- wsparcie zespołu: par@perl.org
Można również przekształcić plik PAR w skrypt zawierający pakiet
- łączy w sobie wszystkie niezbędne obce moduły
- wymaga do uruchomienia na maszynie docelowej jedynie podstawowego
  Perla
- przy wykorzystaniu pp do kompilacji skryptu...
- ...dostaje się program uruchamialny nie wymagający nawet
  podstawowego Perla

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--skipdeps	# make ExtUtils::Autoinstall non-interactive

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS TODO
%{perl_vendorlib}/PAR.pm
%{perl_vendorlib}/PAR/*
%exclude %{perl_vendorlib}/PAR/*.pod
%{_mandir}/man?/*
