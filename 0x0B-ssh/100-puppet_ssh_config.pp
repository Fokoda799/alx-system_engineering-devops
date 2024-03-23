# Client configuration file (w/ Puppet)

file { '~/.ssh/config':
  ensure => present,
  owner  => 'u0_a386',
  group  => 'u0_a386',
  mode   => '0600',
  content => "
    Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
}
