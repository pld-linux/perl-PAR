#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	PAR
Summary:	Perl Archive Toolkit
Name:		perl-%{pnam}
Version:	0.74
Release:	1
License:	Same as Perl itself
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pnam}/%{pnam}-%{version}.tar.gz
# Source0-md5:	646af8c792372c78bcf542799b1e8d9b
URL:		http://par.perl.org
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-Module-ScanDeps
BuildRequires:	perl-PAR-Dist
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
- ...you get an executable not even needing core perl 

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
%attr(755,root,root)/usr/bin/par.pl
# FIXME: conflicts with nss-tools
%attr(755,root,root)/usr/bin/pp
# Do we need "parl" (static => huge)?
%attr(755,root,root)/usr/bin/parldyn
