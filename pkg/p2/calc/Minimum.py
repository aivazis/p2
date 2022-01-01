# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# evaluator that returns the minimum value of its operands
class Minimum:
    """
    The representation of the minimum value of a collection of nodes
    """


    # value management
    def getValue(self):
        """
        Compute and return my value
        """
        # compute and return my value
        return min(operand.getValue() for operand in self.operands)


# end of file
