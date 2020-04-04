%{?scl:%scl_package perl-podlators}

Name:           %{?scl_prefix}perl-podlators
Epoch:          1
Version:        4.12
Release:        3%{?dist}
Summary:        Format POD source into various output formats
# pod/perlpodstyle.pod:     FSFAP
# other files:              GPL+ or Artistic
## Not in the binary package
# t/data/basic.cap:         FSFAP
# t/data/basic.clr:         FSFAP
# t/data/basic.man:         FSFAP
# t/data/basic.ovr:         FSFAP
# t/data/basic.pod:         FSFAP
# t/data/basic.txt:         FSFAP
# t/data/snippets/man/uppercase-license:    MIT
# t/data/snippets/README:   FSFAP
# t/docs/pod.t:             MIT
# t/docs/pod-spelling.t:    MIT
# t/docs/spdx-license.t:    MIT
# t/docs/synopsis.t:        MIT
# t/docs/urls.t:            MIT
# t/lib/Test/RRA.pm:        MIT
# t/lib/Test/RRA/Config.pm:         MIT
# t/lib/Test/RRA/ModuleVersion.pm:  MIT
# t/style/minimum-version.t:        MIT
# t/style/module-version.t:         MIT
# t/style/strict.t:         MIT
License:        (GPL+ or Artistic) and FSFAP
URL:            https://metacpan.org/release/podlators
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRA/podlators-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(:VERSION) >= 5.6
BuildRequires:  %{?scl_prefix}perl(Config)
# Cwd run by PL script in scripts directory
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
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
BuildRequires:  %{?scl_prefix}perl(File::Temp)
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
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Pod::Simple\\)$

%description
This package contains Pod::Man and Pod::Text modules which convert POD input
to *roff source output, suitable for man pages, or plain text.  It also
includes several sub-classes of Pod::Text for formatted output to terminals
with various capabilities.

%prep
%setup -q -n podlators-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 && %{make_build}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}%{make_install}%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING AUTOMATED_TESTING RELEASE_TESTING
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes NOTES README THANKS TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Thu Jan 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:4.12-3
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Petr Pisar <ppisar@redhat.com> - 1:4.12-1
- 4.12 bump

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:4.11-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:4.11-2
- Perl 5.28 rebuild

* Wed May 09 2018 Petr Pisar <ppisar@redhat.com> - 4.11-1
- 4.11 bump
- License changed to (GPL+ or Artistic) and FSFAP

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Petr Pisar <ppisar@redhat.com> - 4.10-1
- 4.10 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.09-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.09-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 08 2016 Petr Pisar <ppisar@redhat.com> - 4.09-1
- 4.09 bump

* Mon Sep 26 2016 Petr Pisar <ppisar@redhat.com> - 4.08-1
- 4.08 bump

* Tue Sep 20 2016 Petr Pisar <ppisar@redhat.com> - 4.07-366
- License declaration corrected to "(GPL+ or Artistic) and MIT"

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
