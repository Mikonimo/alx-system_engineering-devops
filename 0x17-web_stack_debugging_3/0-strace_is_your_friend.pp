# Fixes a WordPress file with wrong name
exec { 'fix-wordpress':
  command => 'mv /var/www/html/wp-setting.php /var/www/html/wp-settings.php',
  path    => ['/bin','/usr/bin'],
  onlyif  => 'test -f /var/www/html/wp-setting.php',
}

# Restart Apache service
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix-wordpress'],
}
