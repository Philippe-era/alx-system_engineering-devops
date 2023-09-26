# The web server installed through the  (w/ Puppet)
package { 'nginx':
  ensure => installed,
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me #!/usr/bin/env bash
# 404 page customation

apt-get update
apt-get install -y nginx
# new directory 
mkdir /etc/nginx/html
# creates files
touch /etc/nginx/html/index.html
# echo Hello world to the index.html
echo "Hello World!" > /etc/nginx/html/index.html
touch /etc/nginx/html/404.html
echo "This is a redirecting page" > /etc/nginx/html/404.html

printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 https://youtu.be/BNmyYzosV-E?si=-Wn2abIY0JnkBRDe permament;
    }

    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart

4-not_found_page_404
;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}



