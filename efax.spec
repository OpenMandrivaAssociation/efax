%define	subver	001114a7

Summary:	A program for faxing using a Class 1, 2 or 2.0 fax modem
Name:		efax
Version:	0.9a
Release:	%mkrel 9
License:	GPL
Group:		Communications
Source0:	http://www.cce.com/efax/download/%{name}-%{version}-%{subver}.tar.bz2
URL:		http://www.cce.com/efax/
Source1:	efax.config.bz2
Patch0:		efax-0.9a-mdkconf.bz2
Patch1:		efax-0.9a-crashpowerpc.patch.bz2
Patch2:		efax-0.9a-faxmail-mime.patch.bz2
Patch3:		efax-0.9a-fax_send.patch.bz2
Patch4:		efax-0.9a-fax_locale.patch.bz2
Patch5:		efax-0.9a_illegalnumber_test.patch.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Efax is a small ANSI C/POSIX program that sends and receives faxes using
any Class 1, 2 or 2.0 fax modem.

You need to install efax if you want to send faxes and you have a
Class 1, 2 or 2.0 fax modem.

%prep
%setup -q -n %{name}-%{version}-%{subver}
%patch0 -p1
%patch1 -p1 -b .crashpowerpc
%patch2 -p1 -b .faxmail-mime
%patch3 -p1 -b .fax_send
%patch4 -p1 -b .fax_locale
%patch5 -p1 -b .fax

find . -type f | xargs perl -p -i -e 's@xloadimage@xli@';

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

make BINDIR=$RPM_BUILD_ROOT%{_bindir} MANDIR=$RPM_BUILD_ROOT%{_mandir} install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/fax.config

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/fax.config
%{_bindir}/fax
%{_bindir}/efax
%{_bindir}/efix
%{_mandir}/man1/fax.1*
%{_mandir}/man1/efax.1*
%{_mandir}/man1/efix.1*
