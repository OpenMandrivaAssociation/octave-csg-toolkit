%global octpkg csg-toolkit

Summary:	A GNU Octave package for analyzing long bone diaphyseal cross sectional geometry
Name:		octave-csg-toolkit
Version:	1.2.3
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://github.com/pr0m1th3as/csg-toolkit
Source0:	https://github.com/pr0m1th3as/csg-toolkit/archive/v%{version}/csg-toolkit-%{version}.tar.gz

BuildRequires:	octave-devel >= 4.2.0
BuildRequires:	octave-io

Requires:	octave(api) = %{octave_api}
Requires:	octave-io

Requires(post): octave
Requires(postun): octave

%description
The present package is based on the long-bone-diaphyseal-CSG-Toolkit and has
been created to simplify its installation and usage from within GNU Octave.

It is based on novel and robust algorithms for calculating the cross-sectional
geometric properties of the diaphyses of humerus, ulna, femur, and tibia bones
represented as a triangular mesh in a Wavefront OBJ file format.

%files
%license COPYING
%doc NEWS README.md
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

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

