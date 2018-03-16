# dahak-bespin

This repo contains scripts that use boto3, the Python API 
provided by AWS, to request AWS resources for running 
dahak workflows.

## About dahak-bespin

See [About.md](/About.md) for more about dahak-bespin.
The short version: dahak-bespin automates allocating
the infrastructure needed to run (and test) dahak workflows.

## Networking Infrastructure

See [Networking.md](/Networking.md) for more about the networking 
details. Short version: one network with one subnet.

## Example Usage

A typical session using bespin
might start with the user asking
for some help. Pass the `--help` flag
or the `help` subcommand to bespin:

```
$ bespin --help

 ___   ____  __   ___   _   _
| |_) | |_  ( (` | |_) | | | |\ |
|_|_) |_|__ _)_) |_|   |_| |_| \|

cloud infrastructure tool for dahak

usage: bespin <command> [<args>]

The most commonly used commands are:
   vpc                  Make a VPC for all the dahak nodes
   security             Make a security group for nodes on the VPC
   spy                  Make a spy monitoring node
   yeti                 Make a yeti worker node

dahak-bespin uses boto3 to wrangle nodes in the cloud and run dahak workflows

positional arguments:
  command     Subcommand to run

optional arguments:
  -h, --help  show this help message and exit
```

This will print out usage information.

The user should start with a VPC:

```
bespin vpc          # get help
bespin vpc build    # build vpc
bespin vpc info     # print info
```

Here is the output of the first command:

```
$ bespin vpc
 ___   ____  __   ___   _   _
| |_) | |_  ( (` | |_) | | | |\ |
|_|_) |_|__ _)_) |_|   |_| |_| \|

cloud infrastructure tool for dahak

usage: bespin vpc <vpc_subcommand>

The vpc subcommands available are:
    vpc build           Build the VPC
    vpc destroy         Tear down the VPC
    vpc info            Print info about the VPC
    vpc stash           Print location of VPC stash files
bespin.py: error: the following arguments are required: vpc_command
```

Next, the user should modify the security group 
that was created for the VPC. 

The user must whitelist IP addresses to access 
the network from them.
IP addresses should be specified in CIDR notation.

The user may also whitelist ports. 
All nodes on the network have whitelisted ports open.
All ports are open only to the VPC and to whitelisted 
IP addresses.

```
bespin security
bespin security port add 9999       # add a port to open
bespin security ip add "8.8.8.8/32" # add an IP to whitelist

bespin security port rm 9090        # close a port
bespin security ip rm "8.8.8.8/32"  # removes an IP from whitelist (if present)
```

(NOTE: security subcommand not yet implemented.)

Now we are ready to add nodes to the VPC.
Start by deploying a spy node:

```
bespin spy          # get help
bespin spy build    # build spy node
bespin spy info     # get info about spy node
```

example output:

```
$ bespin.py spy

 ___   ____  __   ___   _   _
| |_) | |_  ( (` | |_) | | | |\ |
|_|_) |_|__ _)_) |_|   |_| |_| \|

cloud infrastructure tool for dahak

usage: bespin spy <spy_subcommand>

The spy subcommands available are:
    spy build           Build the spy node
    spy destroy         Tear down the spy node
    spy info            Print info about the spy node
    spy stash           Print location of spy stash files
bespin.py: error: the following arguments are required: spy_command
```

Finally, we can deploy a yeti:

```
bespin yeti         # get help
bespin yeti build   # build yeti node
bespin yeti info    # get info about (all) yeti nodes
```

Output from the yeti command:

```
$ bespin yeti
 ___   ____  __   ___   _   _
| |_) | |_  ( (` | |_) | | | |\ |
|_|_) |_|__ _)_) |_|   |_| |_| \|

cloud infrastructure tool for dahak

usage: bespin vpc <vpc_subcommand>

The vpc subcommands available are:
    vpc build           Build the VPC
    vpc destroy         Tear down the VPC
    vpc info            Print info about the VPC
    vpc stash           Print location of VPC stash files
bespin.py: error: the following arguments are required: yeti_command
```

## How Bespin Works

See [HowItWorks.md](/HowItWorks.md)
for a deeper dive into how bespin works.

