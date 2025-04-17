%global octpkg csg-toolkit

Summary:	A GNU Octave package for analyzing long bone diaphyseal cross sectional geometry
Name:		octave-csg-toolkit
Version:	1.4.0
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/csg-toolkit/
Url:		https://github.com/pr0m1th3as/csg-toolkit
Source0:	https://github.com/pr0m1th3as/csg-toolkit/archive/v%{version}/csg-toolkit-%{version}.tar.gz

BuildRequires:	octave-devel >= 7.2.0
BuildRequires:	octave-datatypes >= 1.0.1
BuildRequires:	octave-io >= 2.6.4
BuildRequires:	octave-statistics >= 1.7.4

Requires:	octave(api) = %{octave_api}
Requires:	octave-datatypes >= 1.0.1
Requires:	octave-io >= 2.6.4
Requires:	octave-statistics >= 1.7.4


Requires(post): octave
Requires(postun): octave

%description
The present set of GNU Octave functions provides a novel and robust
algorithm for analyzing the diaphyseal cross-sectional geometric
properties of long bones, which can be applied to any 3D digital
model of a humerus, ulna, femur or tibia bone represented as a
triangular mesh in a Wavefront OBJ file format.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

