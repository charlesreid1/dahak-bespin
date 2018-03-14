#!/usr/local/bin/python3
import argparse
import sys
import dahak_vpc
import dahak_spy

class Boto(object):
    """
    Hat tip:
    https://chase-seibert.github.io/blog/2014/03/21/python-multilevel-argparse.html
    """
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='dahak-bespin uses boto3 to wrangle nodes in the cloud and run dahak workflows',
            usage='''bespin <command> [<args>]

The most commonly used commands are:
   vpc        Make a VPC for all the dahak nodes
   spy        Make a spy monitoring node
   yeti       Make a yeti worker node
''')
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

    def example(self):
        parser = argparse.ArgumentParser(description='Example command description')

        # prefixing the argument with -- means it's optional
        parser.add_argument('--optional', action='store_true')

        # NOT prefixing the argument with -- means it's not optional
        #parser.add_argument('mandatory')

        # now that we're inside a subcommand, ignore the first
        # TWO argvs, ie the command (git) and the subcommand (commit)
        args = parser.parse_args(sys.argv[2:])
        print('Running example, optional=%s' % args.amend)

        #args = parser.parse_args(sys.argv[2:])
        #print('Running example, mandatory=%s' % args.mandatory)


    def vpc(self):
        parser = argparse.ArgumentParser(description='Make a VPC and a security group')
        dahak_vpc.make()

    def spy(self):
        parser = argparse.ArgumentParser(description='Make a spy monitoring node and add it to the VPC')
        dahak_spy.make()

    def yeti(self):
        parser = argparse.ArgumentParser(description='Make a yeti worker node and add it to the VPC')
        dahak_yeti.make()



    def fetch(self):
        parser = argparse.ArgumentParser(
            description='Download objects and refs from another repository')
        # NOT prefixing the argument with -- means it's not optional
        parser.add_argument('repository')
        args = parser.parse_args(sys.argv[2:])
        print('Running git fetch, repository=%s' % args.repository)


if __name__ == '__main__':
    Bespin()
