logo = """
 ___   ____  __   ___   _   _     
| |_) | |_  ( (` | |_) | | | |\ | 
|_|_) |_|__ _)_) |_|   |_| |_| \| 

cloud infrastructure tool for dahak
"""

# ----------------------

bespin_description = "dahak-bespin uses boto3 to wrangle nodes in the cloud and run dahak workflows"
bespin_usage = '''bespin <command> [<args>]

The most commonly used commands are:
   vpc                  Make a VPC for all the dahak nodes
   security             Make a security group for nodes on the VPC
   spy                  Make a spy monitoring node
   yeti                 Make a yeti worker node

'''

# ----------------------

vpc_description = "Make a VPC and a security group"
vpc_usage = '''bespin vpc <vpc_subcommand>

The vpc subcommands available are:
    vpc build           Build the VPC
    vpc destroy         Tear down the VPC
    vpc info            Print info about the VPC
    vpc stash           Print location of VPC stash files

'''

vpc_build_description = "Build the VPC"
vpc_build_usage = '''bespin vpc build [<options>]

The vpc build subcommand does not offer any options.

'''

vpc_destroy_description = "Tear down the VPC"
vpc_destroy_usage = '''bespin vpc destroy [<options>]

The vpc destroy subcommand does not offer any options.

'''

vpc_info_description = "Get VPC info"
vpc_info_usage = '''bespin vpc info [<options>]

The vpc info subcommand does not offer any options.

'''

vpc_stash_description = "Get the VPC stash files"
vpc_stash_usage = '''bespin vpc stash [<options>]

The vpc stash subcommand does not offer any options.

'''

# ----------------------

spy_description = "Make a spy monitoring node and add it to the VPC"
spy_usage = '''bespin spy <spy_subcommand>

The spy subcommands available are:
    spy build           Build the spy node
    spy destroy         Tear down the spy node
    spy info            Print info about the spy node
    spy stash           Print location of spy stash files

'''

spy_build_description = "Build the spy node"
spy_build_usage = '''bespin spy build [<options>]

The spy build subcommand does not offer any options.

'''

spy_destroy_description = "Tear down the spy node"
spy_destroy_usage = '''bespin spy destroy [<options>]

The spy destroy subcommand does not offer any options.

'''

spy_info_description = "Get spy node info"
spy_info_usage = '''bespin spy info [<options>]

The spy info subcommand does not offer any options.

'''

spy_stash_description = "Get the spy node stash files"
spy_stash_usage = '''bespin spy stash [<options>]

The spy stash subcommand does not offer any options.

'''

# ----------------------

yeti_description = "Make a yeti worker node and add it to the VPC"
yeti_usage = '''bespin yeti <spy_subcommand>

The yeti subcommands available are:
    yeti build           Build the yeti node
    yeti destroy         Tear down the yeti node
    yeti info            Print info about the yeti node
    yeti stash           Print location of yeti stash files

'''

yeti_build_description = "Build the yeti node"
yeti_build_usage = '''bespin yeti build [<options>]

The yeti build subcommand does not offer any options.

'''

yeti_destroy_description = "Tear down the yeti node"
yeti_destroy_usage = '''bespin yeti destroy [<options>]

The yeti destroy subcommand does not offer any options.

'''

yeti_info_description = "Get yeti node info"
yeti_info_usage = '''bespin yeti info [<options>]

The yeti info subcommand does not offer any options.

'''

yeti_stash_description = "Get the yeti node stash files"
yeti_stash_usage = '''bespin yeti stash [<options>]

The yeti stash subcommand does not offer any options.

'''

