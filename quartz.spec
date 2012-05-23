%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio

Name: quartz
Summary: quartz lib
Group: Internet/Applications
License: Apache
Version: 2.1.5
Release: 1{?dist}
URL: http://fill.me.in
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

BuildRequires: java >= 0:1.6.0
BuildRequires: ant >= 0:1.7.0
BuildRequires: tomcat6-servlet-2.5-api
BuildRequires: jakarta-commons-httpclient >= 3.1
BuildRequires: log4j
Requires: java >= 0:1.6.0
%define __jar_repack %{nil}

%description
quartz

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
install -m 644 dist/lib/quartz-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/share/java/quartz-%{version}.jar
/usr/share/java/quartz.jar


%changelog
