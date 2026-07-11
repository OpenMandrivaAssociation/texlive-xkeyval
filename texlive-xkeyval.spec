%global tl_name xkeyval
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.10
Release:	%{tl_revision}.1
Summary:	Extension of the keyval package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xkeyval
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xkeyval.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xkeyval.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xkeyval.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is an extension of the keyval package and offers additional
macros for setting keys and declaring and setting class or package
options. The package allows the programmer to specify a prefix to the
name of the macros it defines for keys, and to define families of key
definitions; these all help use in documents where several packages
define their own sets of keys.

