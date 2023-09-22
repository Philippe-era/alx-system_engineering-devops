# script the pkill in the day
exec { 'pkill killmenow' :
    path    => '/bin/',
    command => 'pkill killmenow',
    }

