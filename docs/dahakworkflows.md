# Running Dahak Workflows

To run dahak workflows,
we use the following architecture:

```

+------------------------------------------------------------+
|    AWS                                                     |
|                                                            |
|   +----------------------------------------------------+   |
|   |      AWS VPC                                       |   |
|   |                                                    |   |
|   |  +------------+          +-----------------+       |   |
|   |  |            |          | yeti1           |       |   |
|   |  | spy        |          |  +-----------------+    |   |
|   |  |            |          |  | yeti2        |  |    |   |
|   |  |            |          |  |   +---------------+  |   |
|   |  |            |          |  |   |  yeti3   |  | |  |   |
|   |  |            | <--------+  |   |          |  | |  |   |
|   |  |            | <-----------+   |          |  | |  |   |
|   |  |            | <---------------+          |  | |  |   |
|   |  +------------+          +--|---|----------+  | |  |   |
|   |                             +---|-------------+ |  |   |
|   |                                 +---------------+  |   |
|   |                                                    |   |
|   +----------------------------------------------------+   |
|                                                            |
+------------------------------------------------------------+

```

## Dahak Infrastructure

Dahak workflows will require:

* VPC to connect nodes
* 1 spy node to monitor and log
* 1+ yeti nodes to run workflows

## Dahak Terraform Files

### VPC

The VPC will allocate an IP address space 10.X.0.0/16.

The VPC subnet will allocate an IP address space 10.X.0.0/24.

The VPC will require AWS-provided DNS/DHCP.

The VPC will require an internet gateway.

The VPC will require a routing table pointing to the gateway.

### Spy Node

The spy node will need to run the cloud init scripts
contained in [dahak-spy](https://github.com/charlesreid1/dahak-spy).

### Yeti Node

The spy node will need to run the cloud init scripts
contained in [dahak-yeti](https://github.com/charlesreid1/dahak-yeti).












