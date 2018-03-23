from dahak_aws import AWSObject
from random_labels import random_label, random_ip

import boto3
import collections
import subprocess
import string
import random
import json
from botocore.exceptions import ClientError
from pprint import pprint
from datetime import datetime


"""
Dahak VPC

Create a single VPC with a single subnet,
add an internet gateway, a routing table,
and DHCP+DNS services.

existence of a stashfile indicates existence of a vpc.
build command creates a brand-new vpc, fails if stashfile exists.
no need for a load command - bespin insists on creating its own infrastructure.
delete command needed.
"""


VPCRule = collections.namedtuple("vpc_rule", ["vpc_ip", "subnet_ip"])

class DahakVPC(AWSObject):

    # Constructor:

    def __init__(self, stashfile):
        AWSObject.__init__(self)
        print("initializing dahak vpc")
        self.stashfile = stashfile


    # Public Methods:

    def build(self):
        """
        vpc build process
        bespin (callee) already checks no stashfile
        """
        print("building vpc...")
        self._build_vpc_network()
        print("done building vpc.")

    def destroy(self):
        """
        vpc destroy process
        bespin (callee) already checks for stashfile
        """
        print("destroying vpc...")
        self._destroy_vpc_network()
        print("done destroying vpc.")

    
    # Private Methods:

    def _build_vpc_network(self):
        """
        Make the necessary api calls
        to create the vpc using boto
        """
        print("making vpc network")

        self.base_ip = random_ip()
        self.label = random_label()

        print("    label = %s"%(self.label))
        print("    base_ip = %s"%(self.base_ip))

        vpc_cidr    = self.base_ip.format(addr=0)+"/16"
        subnet_cidr = self.base_ip.format(addr=0)+"/24"
        vpc_label   = self.label + "_vpc"

        # vpc cidr block
        # vpc subnet cidr block
        vpc_rule = VPCRule( vpc_ip = vpc_cidr,
                            subnet_ip = subnet_cidr)

        try:
            # First, create a VPC network
            vpc = self.resource.create_vpc(CidrBlock = vpc_rule.vpc_ip)

            # Enable DNS on the VPC
            response = self.client.modify_vpc_attribute(VpcId=vpc.vpc_id,
                                                EnableDnsSupport={"Value":True})
            response = self.client.modify_vpc_attribute(VpcId=vpc.vpc_id,
                                            EnableDnsHostnames={"Value":True})

            # Create VPC subnet
            subnet = vpc.create_subnet(CidrBlock = vpc_rule.subnet_ip,
                                       AvailabilityZone = 'us-west-1a')

            # Craete a DHCP options set for the VPC to use
            # (amazon-provided DHCP)
            dhcp_options = self.resource.create_dhcp_options(
                    DhcpConfigurations = [{
                        'Key':'domain-name-servers',
                        'Values':['AmazonProvidedDNS']
                    },
                    {
                        'Key': 'domain-name',
                        'Values': ['us-west-1.compute.internal']
                    }]
            )
            dhcp_options.associate_with_vpc(VpcId = vpc.id)

            # Create an internet gateway attached to this VPC
            gateway = self.resource.create_internet_gateway()
            gateway.attach_to_vpc(VpcId = vpc.id)

            # Create a Route table and add the route
            route_table = self.client.create_route_table(VpcId = vpc.vpc_id)
            route_table_id = route_table['RouteTable']['RouteTableId']
            response = self.client.create_route( DestinationCidrBlock = '0.0.0.0/0',
                                                 RouteTableId = route_table_id,
                                                 GatewayId = gateway.internet_gateway_id )

        except ClientError as e:
        
            print("\n")
            print(" X"*20)
            print("FATAL ERROR")
            print("Could not create network due to error:")
            print("-"*20)
            print(e)
            print("-"*20)
            print("\n")

        # vpc information should be saved in a stash file
        self._stash_vpc_info(vpc.id)

        print("\n")
        print("SUCCESS")
        print("Created VPC with the following information:")
        print("   VPC id: %s"%(vpc.id))
        print("   VPC label: %s"%(vpc_label))
        print("  Subnet: (%s)"%(subnet.id))
        print("\n")

    def _stash_vpc_info(self,vpcid):
        """
        Pass Amazon a VPC ID and ask it for a description,
        and store the resulting JSON in the stash file
        """
        print("stashing vpc info")

        try:

            response = self.client.describe_vpcs(VpcIds=[vpcid])
            del response['ResponseMetadata']

            with open(self.stashfile,'w') as f:
                json.dump(response, f, indent=4, sort_keys=True)

        except ClientError as e:


    def _destroy_vpc_network(self):
        """
        Make the necessary api calls
        to destroy the vpc using boto

        If you delete your Amazon VPC using the Amazon VPC console, 
        all its components--such as subnets, security groups, network 
        ACLs, route tables, internet gateways, VPC peering connections,
        and DHCP options--are also deleted. If you use the AWS Command 
        Line Interface (AWS CLI) to delete the Amazon VPC, you must 
        terminate all instances, delete all subnets, delete custom 
        security groups and custom route tables, and detach any 
        internet gateway in the Amazon VPC before you can delete 
        the Amazon VPC.
        """
        with open(self.stashfile,'r') as f:
            vpc_info = json.load(f)

        vpc_id = vpc_info['Vpcs'][0]['VpcId']

        response = self.client.delete_vpc(VpcId = vpc_id)
        print(response)

        subprocess.call(['rm','-f',self.stashfile])






