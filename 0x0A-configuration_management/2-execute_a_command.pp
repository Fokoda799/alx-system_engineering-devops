# Execute a command with Puppet.

exec {'kill killmenow':
    command   => "/usr/bin/pkill 'killmenow'",
}
