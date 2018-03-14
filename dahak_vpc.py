import boto3
import collections
import string
import random
from botocore.exceptions import ClientError
from pprint import pprint
from datetime import datetime

"""
Dahak VPC

Create a single VPC
with a single subnet,
add an internet gateway,
a routing table, and 
DHCP+DNS services.

Create a security group
that allows access to the 
required ports over the VPC.
"""

class DahakVPC(object):

    def __init__(self):
        print("initializing dahak vpc")

    def build(self):
        print("building vpc...")
        self._build_vpc_network()
        self._build_security_group()
        self._stash_vpc_info()
        print("done building vpc.")

    def _build_vpc_network(self):
        print("making vpc network")

    def _build_security_group(self):
        print("making security group")

    def _stash_vpc_info(self):
        print("stashing vpc info")

