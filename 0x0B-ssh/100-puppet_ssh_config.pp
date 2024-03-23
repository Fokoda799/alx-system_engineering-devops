# Client configuration file (w/ Puppet)

file { '~/.ssh/config':
  ensure => file,
  content => "
    Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
}
