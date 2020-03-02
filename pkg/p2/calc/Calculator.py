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
    # the augmented base node
    from .Stem import Stem as base

    # value management
    from .Const import Const as const
    from .Value import Value as value
    # operators get their values through computation
    from .Evaluator import Evaluator as evaluator

    # notification system
    from .Reactor import Reactor as reactor
    from .Observer import Observer as observer
    from .Dependent import Dependent as dependent
    from .Observable import Observable as observable
    from .Dependency import Dependency as dependency


    # metamethods
    def __new__(cls, name, bases, attributes, *, basenode=False, **kwds):
        """
        Build a new class record
        """
        # chain up to get variable, operator, and literal
        node = super().__new__(cls, name, bases, attributes, basenode=basenode, **kwds)

        # if this is not the base node of the hierarchy
        if not basenode:
            # all done
            return node

        # all done
        return node


    # implementation details
    # derivations of the user visible classes
    @classmethod
    def literalDerivation(cls, node):
        """
        Contribute to the list of ancestors of the representation of literals
        """
        # make literals const
        yield cls.const
        # give them storage for a value
        yield cls.value
        # the contribution from {algebra}
        yield from super().literalDerivation(node)
        # all done
        return


    @classmethod
    def operatorDerivation(cls, node):
        """
        Contribute to the list of ancestors of operators
        """
        # operator nodes observe their operands
        yield from cls.observerDerivation(node)
        # they are themselves observable
        yield from cls.observableDerivation(node)
        # they know how to compute their values
        yield cls.evaluator
        # and whatever else {algebra} contributes
        yield from super().operatorDerivation(node)
        # all done
        return


    @classmethod
    def variableDerivation(cls, node):
        """
        Contribute to the list of ancestors of variables
        """
        # variables are observable
        yield from cls.observableDerivation(node)
        # they have storage for a value
        yield cls.value
        # and whatever else {algebra} contributes
        yield from super().variableDerivation(node)
        # all done
        return


    # structural contributions
    @classmethod
    def observableDerivation(cls, node):
        """
        Contribute observable behavior
        """
        # inject value management
        yield cls.dependency
        # and the notification support
        yield cls.observable
        # all done
        return


    @classmethod
    def observerDerivation(cls, node):
        """
        Contribute observer behavior
        """
        # inject value management
        yield cls.dependent
        # and observable management
        yield cls.observer
        # all done
        return


# end of file
