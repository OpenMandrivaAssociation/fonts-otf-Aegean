%define fontname	Aegean
%define name		fonts-otf-%{fontname}
%define version		3.01
%define release		%mkrel 1

%define fontdir		%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Unicode Aegean fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://users.teilar.gr/~g1951d/%{fontname}.zip
Source1:	http://users.teilar.gr/~g1951d/Anatolian.zip
License:	Public Domain
Group:		System/Fonts/Open type
Url:		http://users.teilar.gr/~g1951d/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	mkfontscale, mkfontdir

%description
Aegean covers the following scripts and symbols supported by The
Unicode Standard 5.2: Basic Latin, Greek and Coptic, Greek Extended,
some Punctuation and other Symbols, Linear B Syllabary, Linear B
Ideograms, Aegean Numbers, Ancient Greek Numbers, Ancient Symbols,
Phaistos Disc, Lycian, Carian, Old Italic, Ugaritic, Old Persian,
Cypriot Syllabary, Phoenician, Lydian, and Archaic Greek Musical
Notation. Aegean allocates in the Supplementary Private Use Plane 15,
the following scripts and symbols, as yet unsupported by Unicode:
Cretan Hieroglyphs, Cypro-Minoan, Linear A, the Arkalochori Axe,
Ancient Greek and Old Italic variant alphabets.

In this version:
* Cretan Hieroglyphs are redesigned and expanded to cover signs on
  seals.
* Cypro-Minoan is entirely new and in agreement with the latest
  edition of the inscriptions.
* Idalion, Akanthou, Eteocypriot, Ancient and Recent Paphian variants
  of the Cypriot Syllabary are available as its Open Type Stylistic
  Sets I-V.
* Anatolian Hieroglyphs are included in this package.

%prep
%setup -q -c %{name}-%{version}
unzip %SOURCE1

%install
%__rm -rf %{buildroot}

%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 *.otf %{buildroot}%{fontdir}
mkfontscale %{buildroot}%{fontdir}
mkfontdir %{buildroot}%{fontdir}

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
%{fontconfdir}/otf*
%{fontdir}/*.otf
%{fontdir}/fonts.*

