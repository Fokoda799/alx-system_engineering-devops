# 0. Create a file with Puppet.

file { '/tmp/school':
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
