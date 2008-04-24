
%define name	tmispell-voikko
%define shortname	tmispell
%define version	0.7
%define rel	2

Summary:	Ispell compatible front-end for Voikko
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	GPLv2+
Group:		Text tools
URL:            http://voikko.sourceforge.net/
Source:         http://downloads.sourceforge.net/voikko/%name-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	libncursesw-devel
BuildRequires:	glib2-devel
BuildRequires:	glibmm2.4-devel
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

# (Anssi 04/2008) KDE uses "fi"
sed -r -i 's,^finnish(.*)$,finnish\1\nfi\1,' tmispell.conf.example

%install
rm -rf %{buildroot}
%makeinstall_std

ln -s tmispell %{buildroot}%{_bindir}/ispell

install -d -m755 %{buildroot}%{_sysconfdir}
install -m644 tmispell.conf.example %{buildroot}%{_sysconfdir}/tmispell.conf

# fake Finnish dictionary for ispell clients
install -d -m755 %{buildroot}%{_prefix}/lib/ispell
touch %{buildroot}%{_prefix}/lib/ispell/fi.{hash,aff}

# (anssi 04/2008) KDE searches from libdir instead
%if "%_lib" != "lib"
install -d -m755 %{buildroot}%{_libdir}
ln -s %{_prefix}/lib/ispell %{buildroot}%{_libdir}/ispell
%endif

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README README.fi
%config %{_sysconfdir}/tmispell.conf
%{_bindir}/ispell
%{_bindir}/tmispell
%{_prefix}/lib/ispell
%{_libdir}/ispell
%{_mandir}/man1/tmispell.1*
%{_mandir}/man5/tmispell.conf.5*


