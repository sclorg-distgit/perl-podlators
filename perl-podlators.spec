%{?scl:%scl_package perl-podlators}

Name:           %{?scl_prefix}perl-podlators
Version:        4.07
Release:        366%{?dist}
Summary:        Format POD source into various output formats
# pod/perlpodstyle:         ??? (FSFULLR?)
# other files:              GPL+ or Artistic
## Not in the binary package
# t/docs/pod.t:             MIT
# t/docs/pod-spelling.t:    MIT
# t/docs/synopsis.t:        MIT
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/podlators/
Source0:        http://www.cpan.org/authors/id/R/RR/RRA/podlators-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
# Cwd run by PL script in scripts directory
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# File::Basename run by PL script in scripts directory
BuildRequires:  %{?scl_prefix}perl(File::Basename)
# File::Spec version declared in lib/Pod/Man.pm comment
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.8
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Encode)
BuildRequires:  %{?scl_prefix}perl(Exporter)
# Getopt::Long not used at tests
BuildRequires:  %{?scl_prefix}perl(Pod::Simple) >= 3.06
# Pod::Usage not used at tests
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(subs)
BuildRequires:  %{?scl_prefix}perl(Term::ANSIColor)
BuildRequires:  %{?scl_prefix}perl(Term::Cap)
BuildRequires:  %{?scl_prefix}perl(vars)
# Tests:
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests:
# JSON::PP not used
# Perl::Critic::Utils not used
# Perl6::Slurp not used
BuildRequires:  %{?scl_prefix}perl(PerlIO::encoding)
# Test::MinimumVersion not used
# Test::Pod not used
# Test::Spelling not used
# Test::Strict not used
# Test::Synopsis not used
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(File::Basename)
# File::Spec version declared in lib/Pod/Man.pm comment
Requires:       %{?scl_prefix}perl(File::Spec) >= 0.8
Requires:       %{?scl_prefix}perl(Pod::Simple) >= 3.06
Conflicts:      %{?scl_prefix}perl < 4:5.16.1-234

# Filter under-specified dependencies
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(Pod::Simple)/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Pod::Simple\\)$
%endif

%description
This package contains Pod::Man and Pod::Text modules which convert POD input
to *roff source output, suitable for man pages, or plain text.  It also
includes several sub-classes of Pod::Text for formatted output to terminals
with various capabilities.

%prep
%setup -q -n podlators-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes NOTES README THANKS TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 4.07-366
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.07-365
- Increase release to favour standalone package

* Mon Mar 21 2016 Petr Pisar <ppisar@redhat.com> - 4.07-1
- 4.07 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Petr Pisar <ppisar@redhat.com> - 4.06-1
- 4.06 bump

* Mon Jan 18 2016 Petr Pisar <ppisar@redhat.com> - 4.05-1
- 4.05 bump

* Mon Jan 04 2016 Petr Pisar <ppisar@redhat.com> - 4.04-1
- 4.04 bump

* Mon Dec 07 2015 Petr Pisar <ppisar@redhat.com> - 4.03-1
- 4.03 bump

* Thu Dec 03 2015 Petr Pisar <ppisar@redhat.com> - 4.02-1
- 4.02 bump

* Wed Dec 02 2015 Petr Pisar <ppisar@redhat.com> - 4.01-1
- 4.01 bump

* Tue Dec 01 2015 Petr Pisar <ppisar@redhat.com> - 4.00-1
- 4.00 bump

* Wed Jul 15 2015 Petr Pisar <ppisar@redhat.com> - 2.5.3-347
- Adapt tests to Term-Cap-1.16

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.3-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.3-4
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.3-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 08 2013 Petr Pisar <ppisar@redhat.com> - 2.5.3-1
- 2.5.3 bump

* Mon Sep 23 2013 Petr Pisar <ppisar@redhat.com> - 2.5.2-1
- 2.5.2 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 2.5.1-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.5.1-3
- Link minimal build-root packages against libperl.so explicitly

* Tue Jun 25 2013 Petr Pisar <ppisar@redhat.com> - 2.5.1-2
- Specify all dependencies

* Thu Feb 28 2013 Petr Pisar <ppisar@redhat.com> - 2.5.1-1
- 2.5.1 bump

* Thu Feb 07 2013 Petr Pisar <ppisar@redhat.com> - 2.5.0-2
- Correct dependencies

* Fri Jan 04 2013 Petr Pisar <ppisar@redhat.com> - 2.5.0-1
- 2.5.0 bump
- This version makes pod2* tools failing if POD syntax error is encountered

* Thu Nov 01 2012 Petr Pisar <ppisar@redhat.com> - 2.4.2-3
- Do not export under-specified dependencies

* Wed Oct 31 2012 Petr Pisar <ppisar@redhat.com> - 2.4.2-2
- Conflict perl-podlators with perl before sub-packaging

* Wed Sep 12 2012 Petr Pisar <ppisar@redhat.com> 2.4.2-1
- Specfile autogenerated by cpanspec 1.78.
