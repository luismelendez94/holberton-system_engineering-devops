#Creates Sets up client SSH configuration file
file { 'file exists':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
}

file_line { 'use private key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'disable password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
