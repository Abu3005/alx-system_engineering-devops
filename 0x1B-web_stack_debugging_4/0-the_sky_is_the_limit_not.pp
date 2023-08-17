# The default configuration file for mginx only allows 15 max open files
# this triggers errors when the server receives too many requests
exec {'change limit from 15 to 15000 in /etc/default/nginx':
  command => '/bin/sed -i "s@ULIMIT=\"-n 15\"@ULIMIT=\"-n 15000\"@" /etc/default/nginx && /etc/init.d/nginx restart',
}