# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# externals
import operator
import functools


# evaluator that returns the product of the values of its operands
class Product:
    """
    The representation of the product of nodes
    """


    # value management
    def getValue(self):
        """
        Compute and return my value
        """
        # compute and return my value
        return functools.reduce(operator.mul, (op.getValue() for op in self.operands))


# end of file
