%define PROJECT     rpmdemo 
%define installdir  /usr/local/rpmdemo

Name:	    %{PROJECT}	
Version:	0.0.1
Release:	1
Summary:    hello world 

Group:      System Environment/Daemons	
License:	GPL
URL:		https://github.com/jaygno/rpmdemo
Source0:    %{PROJECT}.tar.gz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: /bin/sh	
Requires:	/bin/sh

%description
hello world

%prep
zcat $RPM_SOURCE_DIR/%{PROJECT}.tar.gz | tar xvf -

%build
cd $RPM_BUILD_DIR/%{PROJECT}/src/
make
install -D hello ../bin/hello

%install
rm -rf %{installdir}

mkdir -p $RPM_BUILD_ROOT/%{installdir}/{bin,conf,logs,sbin}

install -m 0755 -D $RPM_BUILD_DIR/%{PROJECT}/bin/*   $RPM_BUILD_ROOT/%{installdir}/bin/
install -m 0755 -D $RPM_BUILD_DIR/%{PROJECT}/sbin/*  $RPM_BUILD_ROOT/%{installdir}/sbin/
install -m 0755 -D $RPM_BUILD_DIR/%{PROJECT}/conf/*   $RPM_BUILD_ROOT/%{installdir}/conf/
install         -d                                   $RPM_BUILD_ROOT/%{installdir}/logs/

%clean
rm -rf $RPM_BUILD_ROOT

%files

%defattr(0644,nobody,nobody,-)
%{installdir}/logs/

%defattr(0755,nobody,nobody,-)
%{installdir}/bin/

%defattr(0755,nobody,nobody,-)
%{installdir}/sbin/

%defattr(0644,nobody,nobody,-)
%{installdir}/conf/
%config(noreplace) %{installdir}/conf/cfg.json

%postun
if [ $1 -eq 0 ]; then
    rm -rf %{installdir}
elif [ $1 -eq 1 ]; then
    echo "Upgrade.."
fi

%changelog
* Fri Aug  31 2016 jaygno gyunj2013@163.com   
- hello world! 
