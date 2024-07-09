# Custom HTTP header in an Nginx server

# Update Ubuntu server
exec { 'update server':
  command  => '/usr/bin/apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
# Install Nginx web server on the server
package { 'nginx':
  ensure   => present,
  provider => 'apt',
}
->
# Custom Nginx response header (X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By \$hostname;',
}
->
# Start and enable Nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

