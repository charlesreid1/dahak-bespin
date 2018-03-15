# dahak-bespin

This repo contains scripts that use boto3, the Python API 
provided by AWS, to request AWS resources for running 
dahak workflows.

```
               __                        __          
  ____ ___  __/ /_____  ____ ___  ____ _/ /____      
 / __ `/ / / / __/ __ \/ __ `__ \/ __ `/ __/ _ \     
/ /_/ / /_/ / /_/ /_/ / / / / / / /_/ / /_/  __/     
\__,_/\__,_/\__/\____/_/ /_/ /_/\__,_/\__/\___/      
         ____   __  __                               
  ____ _/ / /  / /_/ /_  ___                         
 / __ `/ / /  / __/ __ \/ _ \                        
/ /_/ / / /  / /_/ / / /  __/                        
\__,_/_/_/   \__/_/ /_/\___/                         
   __  __    _                                       
  / /_/ /_  (_)___  ____ ______                      
 / __/ __ \/ / __ \/ __ `/ ___/                      
/ /_/ / / / / / / / /_/ (__  )                       
\__/_/ /_/_/_/ /_/\__, /____/                        
                 /____/                              
```

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
for some help:

```
bespin --help

bespin help
```

This will print out usage information.

The user should start with a VPC:

```
bespin vpc          # get help
bespin vpc build    # build vpc
bespin vpc info     # print info
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

Now we are ready to add nodes to the VPC.
Start by deploying a spy node:

```
bespin spy          # get help
bespin spy build    # build spy node
bespin spy info     # get info about spy node
```

and finally, we can deploy a yeti:

```
bespin yeti         # get help
bespin yeti build   # build yeti node
bespin yeti info    # get info about (all) yeti nodes
```

## How Bespin Works

See [HowItWorks.md](/HowItWorks.md)
for a deeper dive into how bespin works.

