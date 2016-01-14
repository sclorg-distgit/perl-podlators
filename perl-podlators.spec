%{?scl:%scl_package perl-podlators}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-podlators
Version:        2.5.3
Release:        2%{?dist}
Summary:        Format POD source into various output formats
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/podlators/
Source0:        http://www.cpan.org/authors/id/R/RR/RRA/podlators-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.8
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Encode)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(Pod::Simple) >= 3.06
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(subs)
BuildRequires:  %{?scl_prefix}perl(Term::ANSIColor)
BuildRequires:  %{?scl_prefix}perl(Term::Cap)
BuildRequires:  %{?scl_prefix}perl(vars)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests:
BuildRequires:  %{?scl_prefix}perl(PerlIO::encoding)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(File::Basename)
Requires:       %{?scl_prefix}perl(File::Spec) >= 0.8
Requires:       %{?scl_prefix}perl(Pod::Simple) >= 3.06
Conflicts:      %{?scl_prefix}perl < 4:5.16.2-2

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Pod::Simple\\)$

%if ( 0%{?rhel} && 0%{?rhel} < 7 )
%filter_from_requires /perl(Pod::Simple)\s*$/d
%filter_setup
%endif

%description
This package contains Pod::Man and Pod::Text modules which convert POD input
to *roff source output, suitable for man pages, or plain text.  It also
includes several sub-classes of Pod::Text for formatted output to terminals
with various capabilities.

%prep
%setup -q -n podlators-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc ChangeLog NOTES README THANKS TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Jan 06 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.3-2
- Update filters
- Resolves: rhbz#1047918

* Mon Nov 18 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.3-1
- 2.5.3 bump

* Tue May 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.1-1
- 2.5.1 bump

* Wed Feb 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.0-1
- SCL package - initial import
