# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# declaration
class Count:
    """
    The representation of the length of a collection of nodes
    """


    # value management
    def getValue(self):
        """
        Compute and return my value
        """
        # compute and return my value
        return len(tuple(self.operands))


# end of file
