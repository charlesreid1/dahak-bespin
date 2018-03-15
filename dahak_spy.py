from dahak_node import DahakNode


"""
Dahak Spy

Create a spy node for logging and monitoring.

Add it to the VPC.
"""


class DahakSpy(DahakNode):

    def __init__(self):
        DahakNode.__init__(self,"spy")

