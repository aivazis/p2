# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# evaluator for functional nodes
class Evaluator:
    """
    Mix-in class that computes the value of operator nodes by invoking their evaluator on their
    operands
    """


    # value management
    def getValue(self):
        """
        Compute and return my value
        """
        # compute the values of my operands
        values = (op.getValue() for op in self.operands)
        # apply my operator
        return self.evaluator(*values)


# end of file
