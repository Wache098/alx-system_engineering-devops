# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Define a file resource to manage the Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define the Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
}

# Define an Exec resource to retrieve the hostname and add custom header
exec { 'add_custom_http_header':
  command     => "/bin/bash -c 'HOSTNAME=$(hostname); sed -i \"23i add_header X-Served-By \$HOSTNAME;\" /etc/nginx/sites-available/default'",
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
