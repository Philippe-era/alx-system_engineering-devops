# command that allows you to download flask 
package { 'flask' :
    ensure   => '2.1.0',
    provider => 'pip3',
    }

