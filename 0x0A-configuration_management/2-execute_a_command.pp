# This Puppet manifest uses the exec resource to kill a process named killmenow using pkill.
exec { 'kill_killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  path        => '/usr/bin:/bin:/usr/sbin:/sbin',
  refreshonly => true,
}
