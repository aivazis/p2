# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# evaluator that returns the sum of the values of its operands
class Sum:
    """
    The representation of the sum of nodes
    """


    # value management
    def getValue(self):
        """
        Compute and return my value
        """
        # easy enough
        return sum(operand.getValue() for operand in self.operands)


# end of file
