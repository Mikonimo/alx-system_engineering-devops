# 0-strace_is_your_friend.pp

exec { 'fix-wordpress':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => ['/bin','/usr/bin'],
  onlyif  => "grep -q 'class-wp-locale.phpp' /var/www/html/wp-settings.php",
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix-wordpress'],
}