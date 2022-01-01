# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# external
import statistics


# evaluator that computes the mean of the values of a collection of nodes
class Mean:
    """
    The representation of the mean value of a collection of nodes
    """


    # value management
    def getValue(self):
        """
        Compute and return my value
        """
        # compute and return the mean
        return statistics.mean(operand.getValue() for operand in self.operands)


# end of file
