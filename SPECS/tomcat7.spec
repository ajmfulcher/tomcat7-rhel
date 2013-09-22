
%global jspspec 2.1
%global major_version 7
%global minor_version 0
%global micro_version 42
%global servletspec 2.5

# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%global basedir %{_var}/lib/%{name}
%global appdir %{basedir}/webapps
%global logdir %{_var}/log/%{name}
%global homedir %{_datadir}/%{name}
%global cachedir %{_var}/cache/%{name}
%global tempdir %{cachedir}/temp
%global workdir %{cachedir}/work

Name: tomcat7
Epoch: 0
Version: %{major_version}.%{minor_version}.%{micro_version}
Release: 57%{?dist}
Summary: Apache Servlet/JSP Engine, RI for Servlet %{servletspec}/JSP %{jspspec} API

Group: Networking/Daemons
License: ASL 2.0
URL: http://tomcat.apache.org/
Source0:http://www.apache.org/dist/tomcat/tomcat-7/v%{version}/bin/apache-tomcat-%{version}.tar.gz

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License version 2.0. Tomcat is intended
to be a collaboration of the best-of-breed developers from around the world.

%prep
%setup -n apache-tomcat-%{version}

# lrwxrwxrwx 1 root tomcat   12 Sep 21 10:46 conf -> /etc/tomcat6
# lrwxrwxrwx 1 root root     23 Sep 21 10:46 lib -> /usr/share/java/tomcat6
# lrwxrwxrwx 1 root root     16 Sep 21 10:46 logs -> /var/log/tomcat6
# lrwxrwxrwx 1 root root     23 Sep 21 10:46 temp -> /var/cache/tomcat6/temp
# lrwxrwxrwx 1 root root     24 Sep 21 10:46 webapps -> /var/lib/tomcat6/webapps
# lrwxrwxrwx 1 root root     23 Sep 21 10:46 work -> /var/cache/tomcat6/work

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}/usr/share/%{name}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{logdir}
/bin/touch ${RPM_BUILD_ROOT}%{logdir}/catalina.out
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{homedir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{tempdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{workdir}

# Clean the re-pointed directories
%{__rm} -rf ./webapps
%{__rm} -rf ./logs
%{__rm} -rf ./work
%{__rm} -rf ./temp

# Copy the rest of the tomcat package into place
%{__cp} -ar ./* ${RPM_BUILD_ROOT}/usr/share/%{name}/

# symlink to the FHS locations where we've installed things
pushd ${RPM_BUILD_ROOT}%{homedir}
    %{__ln_s} %{appdir} webapps
#    %{__ln_s} %{confdir} conf
#    %{__ln_s} %{libdir} lib
    %{__ln_s} %{logdir} logs
    %{__ln_s} %{tempdir} temp
    %{__ln_s} %{workdir} work
popd

%files
%{homedir}/lib
%{homedir}/conf
%{homedir}/temp
%{homedir}/webapps
%{homedir}/work
%{homedir}/logs
%{homedir}/bin
%{homedir}/LICENSE
%{homedir}/NOTICE
%{homedir}/RELEASE-NOTES
%{homedir}/RUNNING.txt
%{logdir}/catalina.out
%{tempdir}
%{workdir}
%{appdir}

%changelog