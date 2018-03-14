#!/usr/local/bin/python3
import argparse
import sys
from dahak_vpc import DahakVPC
from dahak_spy import DahakSpy
from dahak_yeti import DahakYeti
import long_strings 

class Bespin(object):
    """
    Hat tip:
    https://chase-seibert.github.io/blog/2014/03/21/python-multilevel-argparse.html
    """
    def __init__(self):
        self.logo = long_strings.logo
        print(self.logo)

        self.hasVpc = False
        self.hasSpy = False
        self.hasYeti = False

        parser = argparse.ArgumentParser(
            description=long_strings.bespin_description,
            usage=long_strings.bespin_usage)

        parser.add_argument('command', help='Subcommand to run')

        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
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
        parser = argparse.ArgumentParser(description=long_strings.vpc_description,
                            usage = long_strings.vpc_usage)

        parser.add_argument('vpc_command')

        # ignore first two argvs (command and subcommand)
        args = parser.parse_args(sys.argv[2:])
        print("Received vpc command %s"%(args.vpc_command))

        # use dispatch pattern again, look for method named vpc_command
        vpc_command = "vpc_"+args.vpc_command
        if not hasattr(self, vpc_command):
            print("Unrecognized VPC command")
            parser.print_help()
            exit(1)

        # now invoke the method
        getattr(self, vpc_command)()

    def vpc_build(self):
        """
        Build the VPC
        """
        if(self.hasVpc):
            raise Exception("A VPN already exists!")
        else:
            print("argparser: building vpc")

    def vpc_destroy(self):
        """
        Destroy the VPC
        """
        if(self.hasVpc):
            print("argparser: destroying vpc")
        else:
            raise Exception("No VPN exists! Try creating one with the command:\n\t\tbespin vpn create")

    def vpc_info(self):
        """
        Get information about the VPC
        """
        if(self.hasVpc):
            print("argparser: getting vpc info")
        else:
            raise Exception("No VPN exists.")

    def vpc_stash(self):
        """
        Print the location of stash files 
        for VPC info.
        """
        print("argparser: showing vpc stash")


    ####################################################
    # Node Commands

    def spy(self):
        parser = argparse.ArgumentParser(description='Make a spy monitoring node and add it to the VPC')
        spy = DahakSpy()
        spy.build()

    def yeti(self):
        parser = argparse.ArgumentParser(description='Make a yeti worker node and add it to the VPC')
        yeti = DahakYeti()
        yeti.build()



if __name__ == '__main__':
    Bespin()
