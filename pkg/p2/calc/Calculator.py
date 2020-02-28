# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclass
from .. import algebraic


# the metaclass that constructs the node hierarchy
class Calculator(algebraic.algebra):
    """
    Metaclass that endows algebraic nodes with value management capabilities
    """

    # types
    # value management
    from .Const import Const as const
    from .Value import Value as value
    # operators get their values through computation
    from .Evaluator import Evaluator as evaluator
    # the augmented base node
    # from .Stem import Stem as base


    # metamethods
    def __new__(cls, name, bases, attributes, *, basenode=False, **kwds):
        """
        Build a new class record
        """
        # chain up to get variable, operator, and literal
        record = super().__new__(cls, name, bases, attributes, basenode=basenode, **kwds)

        # if this is not the base node of the hierarchy
        if not basenode:
            # all done
            return record

        # all done
        return record


    # implementation details
    @classmethod
    def literalDerivation(cls, record):
        """
        Contribute to the list of ancestors of the representation of literals
        """
        # make literals const
        yield cls.const
        # give them storage for a value
        yield cls.value
        # the contribution from {algebra}
        yield from super().literalDerivation(record)
        # all done
        return


    @classmethod
    def operatorDerivation(cls, record):
        """
        Contribute to the list of ancestors of operators
        """
        # my operators know how to compute their values
        yield cls.evaluator
        # the contribution from {algebra}
        yield from super().operatorDerivation(record)
        # all done
        return


# end of file
