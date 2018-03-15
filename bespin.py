#!/usr/local/bin/python3
import argparse
import sys
from dahak_vpc import DahakVPC
from dahak_spy import DahakSpy
from dahak_yeti import DahakYeti
import long_strings 


"""
 ___   ____  __   ___   _   _     
| |_) | |_  ( (` | |_) | | | |\ | 
|_|_) |_|__ _)_) |_|   |_| |_| \| 

cloud infrastructure tool for dahak
"""


class Bespin(object):
    """
    Hat tip:
    https://chase-seibert.github.io/blog/2014/03/21/python-multilevel-argparse.html
    """
    def __init__(self):
        self.logo = long_strings.logo
        print(self.logo)

        self.hasVpc = False
        self.hasSecurityGroup = False
        self.hasSpy = False
        self.hasYeti = False

        parser = argparse.ArgumentParser(
            description = long_strings.bespin_description,
            usage = long_strings.bespin_usage)

        parser.add_argument('command', help='Subcommand to run')

        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command: %s\n'%(args.command))
            parser.print_help()
            exit(1)

        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()


    ####################################################
    # VPC Commands

    def vpc(self):
        """
        Process subcommands related to the VPC
        """
        parser = argparse.ArgumentParser(
                description = long_strings.vpc_description,
                usage = long_strings.vpc_usage)

        parser.add_argument('vpc_command')

        # ignore first two argvs (command and subcommand)
        args = parser.parse_args(sys.argv[2:])
        print("Received vpc command %s"%(args.vpc_command))

        # offer to help
        if(args.vpc_command=="help"):
            parser.print_help()
            exit(1)

        # use dispatch pattern again, look for method named vpc_command
        vpc_command = "vpc_"+args.vpc_command
        if not hasattr(self, vpc_command):
            print("Unrecognized VPC command: %s\n"%(args.vpc_command))
            parser.print_help()
            exit(1)

        # now invoke the method
        getattr(self, vpc_command)()


    def vpc_build(self):
        """
        Build the VPC
        """
        if(self.hasVpc):
            raise Exception("A VPC already exists!")
        else:
            print("argparser: building vpc")


    def vpc_destroy(self):
        """
        Destroy the VPC
        """
        if(self.hasVpc):
            print("argparser: destroying vpc")
        else:
            raise Exception("No VPC exists! Try creating one with the command:\n\t\tbespin vpn create")


    def vpc_info(self):
        """
        Get information about the VPC
        """
        if(self.hasVpc):
            print("argparser: getting vpc info")
        else:
            raise Exception("No VPC exists.")


    def vpc_stash(self):
        """
        Print the location of stash files 
        for VPC info.
        """
        print("argparser: showing vpc stash")


    ####################################################
    # Security Group Commands

    def security(self):
        """
        Process subcommands related to the security group
        """
        parser = argparse.ArgumentParser(
                description = long_strings.spy_description,
                usage = long_strings.spy_usage)

        parser.add_argument('security_command')

        args = parser.parse_args(sys.argv[2:])
        print("Received security command %s"%(args.security_command))

        if(args.security_command=="help"):
            parser.print_help()
            exit(1)

        security_command = "security_"+args.vpc_command
        if not hasattr(self, security_command):
            print("Unrecognized security command: %s\n"%(args.security_command))
            parser.print_help()
            exit(1)


    def security_build(self):
        """
        Build the security group
        """
        if(self.hasSecurityGroup):
            raise Exception("A security group already exists!")
        else:
            print("argparser: building security group")


    def security_destroy(self):
        """
        Destroy the security group
        """
        if(self.hasSecurityGroup):
            print("argparser: destroying security group")
        else:
            raise Exception("No security group exists! Try creating one with the command:\n\t\tbespin security create")


    def security_info(self):
        """
        Get information about the security group
        """
        if(self.hasSecurityGroup):
            print("argparser: getting security group info")
        else:
            raise Exception("No security group exists.")


    def security_stash(self):
        """
        Print the location of stash files 
        for security group info.
        """
        print("argparser: showing security group stash")


    ####################################################
    # Spy Node Commands

    def spy(self):
        """
        Process subcommands related to spy
        """
        parser = argparse.ArgumentParser(
                description = long_strings.spy_description,
                usage = long_strings.spy_usage)

        parser.add_argument('spy_command')

        args = parser.parse_args(sys.argv[2:])
        print("Received spy command %s"%(args.spy_command))

        if(args.spy_command=="help"):
            parser.print_help()
            exit(1)

        spy_command = "spy_"+args.spy_command
        if not hasattr(self, spy_command):
            print("Unrecognized spy command: %s\n"%(args.spy_command))
            parser.print_help()
            exit(1)

        getattr(self, spy_command)()


    def spy_build(self):
        """
        Build the spy node
        """
        if(self.hasSpy):
            raise Exception("A spy node already exists!")
        else:
            print("argparser: building spy node")


    def spy_destroy(self):
        """
        Destroy the spy node
        """
        if(self.hasSpy):
            print("argparser: destroying spy node")
        else:
            raise Exception("No spy node exists! Try creating one with the command:\n\t\tbespin spy create")


    def spy_info(self):
        """
        Get information about the spy node
        """
        if(self.hasSpy):
            print("argparser: getting spy node info")
        else:
            raise Exception("No spy node exists.")


    def spy_stash(self):
        """
        Print the location of stash files 
        for spy node info.
        """
        print("argparser: showing spy node stash")


    ####################################################
    # Yeti Node Commands

    def yeti(self):
        """
        Process subcommands related to yeti node
        """
        parser = argparse.ArgumentParser(
                description = long_strings.yeti_description,
                usage = long_strings.vpc_usage)

        parser.add_argument('yeti_command')

        args = parser.parse_args(sys.argv[2:])
        print("Received yeti command %s"%(args.yeti_command))

        if(args.yeti_command=="help"):
            parser.print_help()
            exit(1)

        yeti_command = "yeti_"+args.yeti_command
        if not hasattr(self, yeti_command):
            print("Unrecognized yeti command: %s\n"%(args.yeti_command))
            parser.print_help()
            exit(1)

        getattr(self, yeti_command)()


    def yeti_build(self):
        """
        Build the yeti node
        """
        if(self.hasyeti):
            raise Exception("A yeti node already exists!")
        else:
            print("argparser: building yeti node")

    def yeti_destroy(self):
        """
        Destroy the yeti node
        """
        if(self.hasyeti):
            print("argparser: destroying yeti node")
        else:
            raise Exception("No yeti node exists! Try creating one with the command:\n\t\tbespin yeti create")


    def yeti_info(self):
        """
        Get information about the yeti node
        """
        if(self.hasyeti):
            print("argparser: getting yeti node info")
        else:
            raise Exception("No yeti node exists.")


    def yeti_stash(self):
        """
        Print the location of stash files 
        for yeti node info.
        """
        print("argparser: showing yeti node stash")


if __name__ == '__main__':
    Bespin()

