Name:		texlive-extra
Version:	20100826
Release:	%mkrel 1
Summary:	The TeX formatting system
Group:		Publishing
License:	GPLv2 and BSD and Public Domain and LGPLv2+ and GPLv2+ and LPPL
URL:		http://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100826-extra.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100826-extra.tar.xz.sha256
Source2:	http://linorg.usp.br/CTAN/systems/texlive/tlnet/tlpkg/texlive.tlpdb.xz
Source3:	tlpdb-patch.pl
# tarball of http://linorg.usp.br/CTAN/systems/texlive/tlnet/tlpkg/installer/
# as of 20110214, after removing binaries
Source4:	installer.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

#-----------------------------------------------------------------------
Requires:	perl-Pod-Perldoc
Requires:	perl-Tk
Requires:	texlive
Requires:	texlive-texmf

#-----------------------------------------------------------------------
Patch0:		texlive-20100826-extra-default.patch

#-----------------------------------------------------------------------
%description
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files
%defattr(-,root,root,-)
%{_bindir}/tlmgr
%{_datadir}/texmf/tlpkg
%{_datadir}/texmf/install-tl

#-----------------------------------------------------------------------
%prep
%setup -q -n texlive-20100826-extra
cp %{SOURCE2} .
xz -d texlive.tlpdb.xz

%patch0 -p1

#-----------------------------------------------------------------------
%build
mv texlive.tlpdb{,.orig}
cat texlive.tlpdb.orig | %{SOURCE3} %{_arch} > texlive.tlpdb

#-----------------------------------------------------------------------
%install
mkdir -p %{buildroot}%{_datadir}/texmf/tlpkg/backups
tar jxf %{SOURCE4} -C %{buildroot}%{_datadir}/texmf/tlpkg

cp -far doc.html index.html LICENSE* README release*txt readme*.dir %{buildroot}%{_datadir}/texmf/tlpkg
cp -far tlpkg/* texlive.tlpdb %{buildroot}%{_datadir}/texmf/tlpkg

# not patched for better defaults...
cp -f install-tl %{buildroot}%{_datadir}/texmf

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf ../share/texmf/scripts/texlive/tlmgr.pl tlmgr
popd

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}
