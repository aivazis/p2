# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# mix-in for read-only nodes
class Const:
    """
    Mix-in class that disables setting the value of a node
    """


    # value management
    def setValue(self, value):
        """
        Disable value setting
        """
        # disabled
        raise NotImplementedError("const nodes are read-only")


# end of file
