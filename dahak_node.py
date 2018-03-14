import boto3
import collections
import string
import random
import os, re
import glob
from botocore.exceptions import ClientError
from pprint import pprint
from datetime import datetime

class DahakNode(object):

    def __init__(self,name):
        self.name = name
        print("initializing node %s"%(self.name))

    def build(self):
        print("building node %s..."%(self.name))
        self._build_node_net_interface()
        self._build_node()
        self._stash_node_info()
        print("done building node.")

    def _build_node_net_interface(self):
        print("building node %s network interface"%(self.name))

    def _build_node(self):
        print("building node %s"%(self.name))
    
    def _stash_node_info(self):
        print("stashing node %s info"%(self.name))

