# There is a typ in a php file so the website returns 500
exec { 'sed -i s@.phpp @.php @ /var/www/html/wp-settings.ph':
  command => 'sed  -i "s@.phpp@.php@" /var/www/html/wp-settings.php',
  path    => ['/bin','/sbin','usr/bin','usr/sbin'],
}

# There is a typo in a php file so the website returns 500
# $string1 = "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );"
# $string2 = "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );"

# exec { '/bin/sed -i s@.phpp @.php @ /var/www/html/wp-settings.ph':
#  command => "/bin/sed  -i \"s@$string1@$string2@\" /var/www/html/wp-settings.php",
#  onlyif  => 'test ! -f /var/www/html/wp-settings.php',
# }

# service { 'apache2':
#  ensure => running,
# }