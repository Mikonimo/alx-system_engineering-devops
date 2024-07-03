# Install the Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
}

# Create the Hello World! index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure the Nginx site for the root and /redirect_me
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx_config/default.erb'),
  notify  => Service['nginx'],
}

# Create the Nginx configuration template file
file { '/etc/puppetlabs/code/environments/production/modules/nginx_config/templates/default.erb':
  ensure  => file,
  content => @("EOF"/L)
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html;
    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location = /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
  | EOF
}
