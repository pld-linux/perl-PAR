#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	PAR
Summary:	Perl Archive Toolkit
Summary(pl):	Zestaw narzêdzi perlowych do archiwizacji
Name:		perl-%{pnam}
Version:	0.75
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pnam}/%{pnam}-%{version}.tar.gz
# Source0-md5:	273514ed60806cf9a66c922919a12bb4
URL:		http://par.perl.org
BuildRequires:	perl-Archive-Zip >= 1.00
BuildRequires:	perl-Module-ScanDeps >= 0.30
BuildRequires:	perl-PAR-Dist >= 0.05
BuildRequires:	perl-base >= 5.8.0
BuildRequires:	perl-devel >= 5.8.0
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

%description -l pl
Perl Archive Toolkit:
- robi to samo, co JAR (archiwizator Javy), ale dla Perla
- u¿ywa niezale¿nego od platformy, formatu pliku skompresowanego (zip)
- integruje w jeden plik modu³y, skrypty i inne pliki
- pliki PAR s± ³atwe do wygenerowania, aktualizacji i rozpakowania
Korzy¶ci p³yn±ce ze stosowania PAR:
- skrócenie czasu pobierania i wdro¿enia programu
- oszczêdno¶æ miejsca na dysku wynikaj±ca z kompresji i wybiórczego
  pakietowania
- spójno¶æ wersji: rozwi±zuje problemy zgodno¶ci w przód
- wsparcie zespo³u: par@perl.org
Mo¿na równie¿ przekszta³ciæ plik PAR w skrypt zawieraj±cy pakiet
- ³±czy w sobie wszystkie niezbêdne obce modu³y
- wymaga do uruchomienia na maszynie docelowej jedynie podstawowego
  Perla
- przy wykorzystaniu pp do kompilacji skryptu...
- ...dostaje siê program uruchamialny nie wymagaj±cy nawet
  podstawowego Perla

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ChangeLog AUTHORS
%{perl_vendorlib}/PAR.pm
%{perl_vendorlib}/PAR/*.pm
%{perl_vendorlib}/App/Packer/*.pm
# TODO: App::Packer::PAR
%{_mandir}/man3/*
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/par.pl
# FIXME: conflicts with nss-tools
%attr(755,root,root) %{_bindir}/pp
# Do we need "parl" (static => huge)?
%attr(755,root,root) %{_bindir}/parldyn
