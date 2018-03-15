from dahak_aws import AWSObject

import collections
import string
import random
from pprint import pprint
from datetime import datetime


"""
Dahak Security Group

Create a security group
that allows access to the 
required ports over the VPC.
"""


class DahakSecurity(AWSObject):

    def __init__(self):
        print("initializing dahak security group")

    def build(self):
        print("building security group...")
        self._build_security_group()
        self._stash_security_info()
        print("done building security group.")

    def _build_security_network(self):
        print("making security network")

    def _stash_security_info(self):
        print("stashing security info")

