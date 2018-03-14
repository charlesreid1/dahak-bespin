logo = """
 ___   ____  __   ___   _   _     
| |_) | |_  ( (` | |_) | | | |\ | 
|_|_) |_|__ _)_) |_|   |_| |_| \| 

cloud infrastructure tool for dahak
"""

bespin_description = "dahak-bespin uses boto3 to wrangle nodes in the cloud and run dahak workflows"
bespin_usage = '''bespin <command> [<args>]

The most commonly used commands are:
   vpc        Make a VPC for all the dahak nodes
   spy        Make a spy monitoring node
   yeti       Make a yeti worker node

'''

vpc_description = "Make a VPC and a security group"
vpc_usage = '''bespin vpc <vpc_subcommand>

The vpc subcommands available are:
    vpc build           Build the VPC
    vpc destroy         Tear down the VPC
    vpc info            Print info about the VPC
    vpc stash           Print location of VPC stash files

'''

