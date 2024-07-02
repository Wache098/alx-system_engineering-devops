# This Puppet script configures the SSH client to use the private key ~/.ssh/school and refuse password authentication

file_line { 'IdentityFile':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#?IdentityFile',
}

file_line { 'PasswordAuthentication':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}
