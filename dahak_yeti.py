from dahak_node import DahakNode

"""
Dahak Yeti

Create a yeti node for logging and monitoring.

Add it to the VPC.
"""

class DahakYeti(DahakNode):

    def __init__(self):
        DahakNode.__init__(self,"yeti")

