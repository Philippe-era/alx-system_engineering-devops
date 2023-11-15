# requests will be increased 
#open requests to be checked out

exec { 'set_ulimit_to 5000':
  command => '/bin/sed -i "s/ULIMIT.*/ULIMIT=\"-n 5000\"/" /etc/default/nginx',
#path modification
  path => '/usr/local/bin/:/bin/',


} -> exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  path    => '/etc/init.d/',
}
