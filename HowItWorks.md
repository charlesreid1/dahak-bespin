# How Bespin Works

Bespin is a command line utility 
built around argparser.

Argparser provides a nice suite
of Python tools for extracting
command line arguments and 
processing them.

Dahak has four principal tasks:
* Build a virtual private cloud (VPC) network
* Create a security group to control access to the network
* Create a spy node and add it to the VPC
* Create one or more yeti nodes and add them to the VPC

bespin provides subcommands for each task.
The vpc, spy, and yeti subcommand options
all look pretty similar. 
The security subcommand options are 
different, as the security group is 
created or destroyed with the VPC
(not by the user), but the user 
must still modify the security group
to whitelist IPs and open/close ports.

