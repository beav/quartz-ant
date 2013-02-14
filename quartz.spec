%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio

Name: quartz
Summary: Quartz Enterprise Job Scheduler
License: ASL 2.0
URL: http://www.quartz-scheduler.org/
Group: Development/Libraries/Java
Version: 2.1.5
Release: 4%{?dist}
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

BuildRequires: java >= 0:1.6.0
BuildRequires: ant >= 0:1.7.0
BuildRequires: tomcat6-servlet-2.5-api
BuildRequires: glassfish-javamail
BuildRequires: geronimo-specs
BuildRequires: slf4j
BuildRequires: c3p0
BuildRequires: jakarta-commons-httpclient >= 3.1
BuildRequires: log4j
Requires: java >= 0:1.6.0
%define __jar_repack %{nil}

%description
Quartz is a job scheduling system that can be integrated with, or used
along side virtually any J2EE or J2SE application. Quartz can be used
to create simple or complex schedules for executing tens, hundreds, or
even tens-of-thousands of jobs; jobs whose tasks are defined as standard
Java components or EJBs.

%package -n quartz2-candlepin
Summary: Quartz Enterprise Job Scheduler (build dep for candlepin)

%description -n quartz2-candlepin
A version of quartz that is only used by candlepin. This is to allow Quartz 1.8
and Quartz 2.1 to co-exist on the same system until applications using 1.8 can
upgrade.

%prep
%setup -q

%build
ant -Dlibdir=/usr/share/java -Dversion=%{version} clean package

%install
rm -rf $RPM_BUILD_ROOT
# Create the directory structure required to lay down our files
# common
install -d -m 755 $RPM_BUILD_ROOT/usr/share/java/
ln -s /usr/share/java/quartz-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/quartz.jar
ln -s /usr/share/java/quartz-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/quartz2.jar
install -m 644 dist/lib/quartz-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/share/java/quartz-%{version}.jar
/usr/share/java/quartz.jar

%files -n quartz2-candlepin
/usr/share/java/quartz-%{version}.jar
/usr/share/java/quartz2.jar


%changelog
* Thu May 31 2012 Chris Duryee (beav) <cduryee@redhat.com>
- better specfile description (cduryee@redhat.com)

* Thu May 31 2012 Chris Duryee (beav) <cduryee@redhat.com>
- add build deps (cduryee@redhat.com)

* Wed May 23 2012 Chris Duryee (beav) <cduryee@redhat.com>
- this char breaks rpm building (cduryee@redhat.com)

* Wed May 23 2012 Chris Duryee (beav) <cduryee@redhat.com>
- new package built with tito

