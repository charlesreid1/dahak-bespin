import boto3
from botocore.exceptions import ClientError


"""
AWS Object (Base Class)

Define a base class that has a reference
to an AWS session, resource, and client.
"""


class AWSObject(object):
    """
    AWSObject defines a session, resource, and client
    that are used to make API calls to AWS.
    """
    def __init__(self):
        print("initializing aws object")
        self.session = boto3.Session(region_name="us-west-1")
        self.resource = self.session.resource('ec2') # high level interface
        self.client = self.session.client('ec2') # low level interface

