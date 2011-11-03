# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xkeyval
# catalog-date 2008-08-13 18:44:56 +0200
# catalog-license lppl
# catalog-version 2.6a
Name:		texlive-xkeyval
Version:	2.6a
Release:	1
Summary:	Extension of the keyval package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xkeyval
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xkeyval.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xkeyval.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xkeyval.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package is an extension of the keyval package and offers
additional macros for setting keys and declaring and setting
class or package options. The package allows the programmer to
specify a prefix to the name of the macros it defines for keys,
and to define families of key definitions; these all help use
in documents where several packages define their own sets of
keys.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/xkeyval/keyval.tex
%{_texmfdistdir}/tex/generic/xkeyval/pst-xkey.tex
%{_texmfdistdir}/tex/generic/xkeyval/xkeyval.tex
%{_texmfdistdir}/tex/generic/xkeyval/xkvtxhdr.tex
%{_texmfdistdir}/tex/latex/xkeyval/pst-xkey.sty
%{_texmfdistdir}/tex/latex/xkeyval/xkeyval.sty
%{_texmfdistdir}/tex/latex/xkeyval/xkvltxp.sty
%{_texmfdistdir}/tex/latex/xkeyval/xkvview.sty
%doc %{_texmfdistdir}/doc/latex/xkeyval/README
%doc %{_texmfdistdir}/doc/latex/xkeyval/xkeyval.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xkeyval/xkeyval.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}