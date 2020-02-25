# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclass
from .. import algebraic


# declaration
class Calculator(algebraic.algebra):
    """
    Metaclass that endows nodes with value management capabilities
    """


    # metamethods
    def __new__(cls, name, bases, attributes, *, basenode=False, **kwds):
        """
        Build a new class record
        """
        # chain up
        record = super().__new__(cls, name, bases, attributes, basenode=basenode, **kwds)

        # if this is not the base node of the hierarchy
        if not basenode:
            # all done
            return record

        # all done
        return record


# end of file
