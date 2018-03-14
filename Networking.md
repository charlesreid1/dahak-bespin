# The Network

We use a virtual private cloud (VPC) to allow AWS compute nodes
to talk to one another.

All VPCs define a network, but that is still too wide,
so we have to narrow down the definition and define a subnet.
We can add as many subnets as IPv4 will allow us, but here
we just use one subnet. All our AWS nodes will live on the 
same virtual private cloud subnet. 

We add one monitoring node (dahak spy) and one or more
worker nodes (dahak yeti) to the VPC subnet. All nodes 
run netdata and the monitoring node uses Prometheus to
collect data across the VPC subnet.

Machines on the VPC have the ability to reach the internet, 
are not accessible to the public unless given a public
IP address. Various services can be configured to listen for 
traffic to a particular IP address (by binding the service
to a particular IP address), thus securing databases 
or web servers from access by any traffic not originating
from the private network.

# Creating the Network

## Diagram

The following diagram shows a sechematic of the network architecture:

```
         +--------------------------------------------------------------------------+
         | Whole Internet                                                           |
         |                                                                          |
         |                                                                          |
         |  +--------------------------------------------------------------------+  |
         |  |  Amazon                                                            |  |
         |  |                                                                    |  |
         |  |                                                                    |  |
         |  |                                                                    |  |
         |  |   +---------------------------------------------------+            |  |
         |  |   |   Virtual Private Cloud: Dahak WAN                |            |  |
         |  |   |                                             +-----+-----+      |  |
         |  |   |   Network IP Block: 10.117.0.0/16           | Internet  |      |  |
         |  |   |                     10.117.*.*              | Gateway   |      |  |
         |  |   |                                             +-----+-----+      |  |
         |  |   |    +----------------------------------+           |            |  |
         |  |   |    |  VPC Subnet: Dahak LAN           |           |            |  |
         |  |   |    |                                  |     +-----+-----+      |  |
         |  |   |    |  Subnet IP Block: 10.117.0.0/24  |     |  Routing  |      |  |
         |  |   |    |                   10.117.0.*     |     |  Table    |      |  |
         |  |   |    |                                  |     +-----+-----+      |  |
         |  |   |    |                                  |           |            |  |
         |  |   |    +----------------------------------+           |            |  |
         |  |   |                                             +-----+-----+      |  |
         |  |   |                                             |   DHCP    |      |  |
         |  |   |                                             +-----+-----+      |  |
         |  |   |                                                   |            |  |
         |  |   +---------------------------------------------------+            |  |
         |  |                                                                    |  |
         |  +--------------------------------------------------------------------+  |
         |                                                                          |
         +--------------------------------------------------------------------------+
```


## IP Address Blocks

The IP address schema for the network is `10.X.0.0/16`, indicating 
any IP address of the form `10.X.*.*` (where X is a number between 2 and 253).
For example, `10.117.0.0/16` would cover `10.117.*.*`.

The subnet IP address schema is `10.X.Y.0/24`, indicating
an IP address of the form `10.X.Y.*`. X and Y are any numbers
beteween 2 and 253.

## Internet Gateway

For nodes on the network to be able to reach the internet,
an internet gateway must be added to the VPC. This provides
a way for requests that go out to the internet and make it 
back to the VPC have a way to be rerouted internally to the 
originating node.

This is required for the network we are setting up.

## Routing Table

The routing table defines how computers on the VPC can find
one another and the internet gateway. 

This is required for the network we are setting up.

## DHCP (and DNS)

DHCP and DNS have to do with getting directions and finding things
in IP space. DHCP controls how IP addresses are handed out on a 
network and how to route traffic to nodes on the network. 
DNS has to do with how to turn a web address to an IP address 
and get directions to that IP address. Amazon offers a 
DHCP+DNS service (or you can roll your own, if you're into 
that kind of thing).

This is required for the network we are setting up.

## Adding Nodes

Now, to add nodes, we just add them to the subnet.
They will all be assigned IP addresses of `10.X.0.*`.
For example, 

```
10.117.0.100        spy 
10.117.0.101        yeti #1
10.117.0.102        yeti #2
10.117.0.103        yeti #3
10.117.0.104        yeti #4
```

