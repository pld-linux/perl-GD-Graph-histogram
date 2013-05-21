%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	Graph-histogram
Summary:	GD::Graph::histogram Perl module - Histogram plotting module
Name:		perl-GD-Graph-histogram
Version:	1.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	633c97212412d0d85bb3dc7251f5bad9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-GD-Graph
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Graph::histogram extends the GD::Graph module to create
histograms.  The module allow creation of count or percentage
histograms.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo
%{perl_vendorlib}/GD/Graph/histogram.pm
%{_mandir}/man3/*
