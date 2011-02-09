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
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

#-----------------------------------------------------------------------
Requires:	perl-Pod-Perldoc
Requires:	perl-Tk
Requires:	texlive-texmf

#-----------------------------------------------------------------------
Patch0:		texlive-20100826-extra-default.patch

#-----------------------------------------------------------------------
%description
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system with
binaries for most flavors of Unix, including GNU/Linux, and also
Windows. It includes all the major TeX-related programs, macro
packages, and fonts that are free software, including support for
many languages around the world.

%files
%defattr(-,root,root,-)
%{_datadir}/texmf/tlpkg

#-----------------------------------------------------------------------
%prep
%setup -q -n texlive-20100826-extra
cp %{SOURCE2} .
xz -d texlive.tlpdb.xz

%patch0 -p1

#-----------------------------------------------------------------------
%build

#-----------------------------------------------------------------------
%install
mkdir -p %{buildroot}%{_datadir}/texmf/tlpkg/{backups,installer}

cat > %{buildroot}%{_datadir}/texmf/tlpkg/installer/config.guess << EOF
#!/bin/sh

echo linux-%{_arch}-mandriva
EOF
chmod +x %{buildroot}%{_datadir}/texmf/tlpkg/installer/config.guess

cp -far doc.html index.html LICENSE* README release*txt readme*.dir %{buildroot}%{_datadir}/texmf/tlpkg
cp -far tlpkg/* %{buildroot}%{_datadir}/texmf/tlpkg

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}
