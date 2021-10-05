# Script allows multiple petitons at the same time in a nginx server
exec { 'sed':
  command => "sed -i '5s/.*/ULIMIT=\"-n 2000\"/' /etc/default/nginx",
  path    => '/bin'
}
