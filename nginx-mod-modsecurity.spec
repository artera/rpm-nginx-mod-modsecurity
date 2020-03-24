Summary: ModSecurity v3 Nginx Connector (module for nginx)
Name: nginx-mod-modsecurity
Version: 1.0.0
Release: 3%{?dist}
Vendor: Artera
URL: https://github.com/SpiderLabs/ModSecurity-nginx

%define _modname            modsecurity
%define _nginxver           1.16.1
%define nginx_config_dir    %{_sysconfdir}/nginx
%define nginx_build_dir     %{_builddir}/nginx-%{_nginxver}

Source0: https://nginx.org/download/nginx-%{_nginxver}.tar.gz
Source1: https://github.com/SpiderLabs/ModSecurity-nginx/releases/download/v%{version}/%{_modname}-nginx-v%{version}.tar.gz

Requires: nginx = 1:%{_nginxver}
Requires: libmodsecurity
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libmodsecurity-devel
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel
BuildRequires: perl-devel

License: GPL3

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
ModSecurity v3 Nginx Connector (module for nginx).

%prep
%setup -q -n nginx-%{_nginxver}
%setup -T -D -b 1 -n %{_modname}-nginx-v%{version}

%build
cd %{_builddir}/nginx-%{_nginxver}
./configure %(nginx -V 2>&1 | grep 'configure arguments' | sed -r 's@^[^:]+: @@') --add-dynamic-module=../%{_modname}-nginx-v%{version}
make modules

%install
%{__rm} -rf %{buildroot}

%{__install} -Dm755 %{nginx_build_dir}/objs/ngx_http_modsecurity_module.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_http_modsecurity_module.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nginx/modules/*.so
