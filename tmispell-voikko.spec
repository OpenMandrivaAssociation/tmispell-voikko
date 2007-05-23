
%define name	tmispell-voikko
%define shortname	tmispell
%define version	0.6.2
%define rel	1

Summary:	Ispell compatible front-end for Voikko
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	GPL
Group:		Text tools
URL:            http://voikko.sourceforge.net/
Source:         http://downloads.sourceforge.net/voikko/%name-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	ncurses-devel
BuildRequires:	glib2-devel
BuildRequires:	voikko-devel
Conflicts:	ispell
# Only Finnish is supported currently, remove these if more are added
Provides:	ispell-fi
Requires:	locales-fi
Requires:	voikko-dictionary

%description
Tmispell is an Ispell compatible front-end for spell-checking
modules. To do the actual spell-checking for Finnish language it
uses the spell-checking system Voikko.

Since tmispell-voikko imitates ispell, you have to configure the
relevant program to use ispell for spell-checking and select
dictionary "suomi" or "Finnish".

%prep
%setup -q

%build
%configure2_5x --disable-enchant
%make

%install
rm -rf %{buildroot}
%makeinstall_std

ln -s tmispell %{buildroot}%{_bindir}/ispell

install -d -m755 %{buildroot}%{_sysconfdir}
install -m644 tmispell.conf.example %{buildroot}%{_sysconfdir}/tmispell.conf

# fake Finnish dictionary for ispell clients
install -d -m755 %{buildroot}%{_prefix}/lib/ispell
touch %{buildroot}%{_prefix}/lib/ispell/suomi.{hash,aff}

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog LUEMINUT NEWS README
%config %{_sysconfdir}/tmispell.conf
%{_bindir}/ispell
%{_bindir}/tmispell
%{_prefix}/lib/ispell
%{_mandir}/man1/tmispell.1*
%{_mandir}/man5/tmispell.conf.5*


