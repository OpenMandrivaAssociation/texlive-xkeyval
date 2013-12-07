# revision 27995
# category Package
# catalog-ctan /macros/latex/contrib/xkeyval
# catalog-date 2012-01-23 12:21:58 +0100
# catalog-license lppl
# catalog-version 2.6a
Name:		texlive-xkeyval
Version:	2.6a
Release:	6
Summary:	Extension of the keyval package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xkeyval
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xkeyval.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xkeyval.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xkeyval.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is an extension of the keyval package and offers
additional macros for setting keys and declaring and setting
class or package options. The package allows the programmer to
specify a prefix to the name of the macros it defines for keys,
and to define families of key definitions; these all help use
in documents where several packages define their own sets of
keys.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
