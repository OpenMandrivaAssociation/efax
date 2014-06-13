%define	subver	001114a7

Summary:	A program for faxing using a Class 1, 2 or 2.0 fax modem
Name:		efax
Version:	0.9a
Release:	22
License:	GPLv2
Group:		Communications
Url:		http://www.cce.com/efax/
Source0:	http://www.cce.com/efax/download/%{name}-%{version}-%{subver}.tar.bz2
Source1:	efax.config.bz2
Patch0:		efax-0.9a-mdkconf.patch
Patch1:		efax-0.9a-crashpowerpc.patch
Patch2:		efax-0.9a-faxmail-mime.patch
Patch3:		efax-0.9a-fax_send.patch
Patch4:		efax-0.9a-fax_locale.patch
Patch5:		efax-0.9a_illegalnumber_test.patch
Patch6:		efax-0.9a-fix-str-fmt.patch
Patch7:		efax-0.9a-nostrip.patch

%description
Efax is a small ANSI C/POSIX program that sends and receives faxes using
any Class 1, 2 or 2.0 fax modem.

You need to install efax if you want to send faxes and you have a
Class 1, 2 or 2.0 fax modem.

%prep
%setup -qn %{name}-%{version}-%{subver}
%apply_patches

find . -type f | xargs perl -p -i -e 's@xloadimage@xli@';

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

make BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir} install

mkdir -p %{buildroot}%{_sysconfdir}
bzcat %{SOURCE1} > %{buildroot}%{_sysconfdir}/fax.config

%files
%doc README
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/fax.config
%{_bindir}/fax
%{_bindir}/efax
%{_bindir}/efix
%{_mandir}/man1/fax.1*
%{_mandir}/man1/efax.1*
%{_mandir}/man1/efix.1*

