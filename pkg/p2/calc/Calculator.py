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

    # locally defined user visible classes
    # containers
    from .List import List as list
    from .Set import Set as set
    from .Tuple import Tuple as tuple
    from .Sequence import Sequence as sequence

    # entities that support evaluation after name resolution
    from .Expression import Expression as expression
    from .Interpolation import Interpolation as interpolation
    from .Unresolved import Unresolved as unresolved

    # local operators
    from .Count import Count as count
    from .Maximum import Maximum as maximum
    from .Mean import Mean as mean
    from .Minimum import Minimum as minimum
    from .Product import Product as product
    from .Sum import Sum as sum

    # node probes
    from .Probe import Probe as probe

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

        # name resolution
        # expressions
        node.expression = cls.make(name="expression", base=node,
                                   chain=cls.expressionDerivation(node))
        # interpolations
        node.interpolation = cls.make(name="interpolation", base=node,
                                      chain=cls.interpolationDerivation(node))
        # unresolved nodes
        node.unresolved = cls.make(name="unresolved", base=node,
                                   chain=cls.unresolvedDerivation(node))

        # containers
        node.list = cls.make(name="list", base=node, chain=cls.listDerivation(node))
        node.set = cls.make(name="set", base=node, chain=cls.setDerivation(node))
        node.tuple = cls.make(name="tuple", base=node, chain=cls.tupleDerivation(node))

        # local functional nodes
        # count
        node.count = cls.make(name="count", base=node,
                              chain=cls.functionalDerivation(func=cls.count, node=node))
        # maximum
        node.maximum = cls.make(name="maximum", base=node,
                                chain=cls.functionalDerivation(func=cls.maximum, node=node))
        # mean
        node.mean = cls.make(name="mean", base=node,
                             chain=cls.functionalDerivation(func=cls.mean, node=node))
        # minimum
        node.minimum = cls.make(name="minimum", base=node,
                                chain=cls.functionalDerivation(func=cls.minimum, node=node))
        # product
        node.product = cls.make(name="product", base=node,
                                chain=cls.functionalDerivation(func=cls.product, node=node))
        # sum
        node.sum = cls.make(name="sum", base=node,
                            chain=cls.functionalDerivation(func=cls.sum, node=node))

        # probe
        node.probe = cls.make(name="probe", base=node, chain=cls.probeDerivation(node))

        # all done
        return node


    # implementation details
    # containers
    @classmethod
    def listDerivation(cls, node):
        """
        Contribute to the pile of ancestors of {list} nodes
        """
        # lists observe their operands
        yield from cls.observerDerivation(node)
        # they are themselves observable
        yield from cls.observableDerivation(node)

        # realized container: if the record has an opinion
        if node.list:
            # add it to the pile
            yield node.list
        # the list base class
        yield cls.list

        # abstract container: if the record has an opinion
        if node.sequence:
            # add it to the pile
            yield node.sequence
        # the sequence base class
        yield cls.sequence

        # and whatever else my superclass says
        yield from cls.compositeDerivation(node)
        # all done
        return


    @classmethod
    def setDerivation(cls, node):
        """
        Contribute to the pile of ancestors of {set} nodes
        """
        # sets observe their operands
        yield from cls.observerDerivation(node)
        # they are themselves observable
        yield from cls.observableDerivation(node)

        # realized container: if the record has an opinion
        if node.set:
            # add it to the pile
            yield node.set
        # the set base class
        yield cls.set

        # abstract container: if the record has an opinion
        if node.sequence:
            # add it to the pile
            yield node.sequence
        # the sequence base class
        yield cls.sequence

        # and whatever else my superclass says
        yield from cls.compositeDerivation(node)
        # all done
        return


    @classmethod
    def tupleDerivation(cls, node):
        """
        Contribute to the pile of ancestors of {tuple} nodes
        """
        # tuples observe their operands
        yield from cls.observerDerivation(node)
        # they are themselves observable
        yield from cls.observableDerivation(node)

        # realized container: if the record has an opinion
        if node.tuple:
            # add it to the pile
            yield node.tuple
        # the tuple base class
        yield cls.tuple

        # abstract container: if the record has an opinion
        if node.sequence:
            # add it to the pile
            yield node.sequence
        # the sequence base class
        yield cls.sequence

        # and whatever else my superclass says
        yield from cls.compositeDerivation(node)
        # all done
        return


    # name resolution nodes
    # expressions
    @classmethod
    def expressionDerivation(cls, node):
        """
        Contribute to the list of ancestors of the representation of {expression} nodes
        """
        # expressions observe their operands
        yield from cls.observerDerivation(node)
        # they are themselves observable
        yield from cls.observableDerivation(node)
        # if the record has anything to say
        if node.expression:
            # add it to the pile
            yield node.expression
        # the expression base class
        yield cls.expression
        # expressions are composites
        yield from cls.compositeDerivation(node)
        # all done
        return


    # interpolations
    @classmethod
    def interpolationDerivation(cls, node):
        """
        Contribute to the list of ancestors of the representation of {interpolation} nodes
        """
        # interpolations observe their operands
        yield from cls.observerDerivation(node)
        # they are themselves observable
        yield from cls.observableDerivation(node)
        # if the record has anything to say
        if node.interpolation:
            # add it to the pile
            yield node.interpolation
        # the interpolation base class
        yield cls.interpolation
        # interpolations are composites
        yield from cls.compositeDerivation(node)
        # all done
        return


    # unresolved
    @classmethod
    def unresolvedDerivation(cls, node):
        """
        Contribute to the list of ancestors of the representation of {unresolved} nodes
        """
        # my unresolved nodes are observable
        yield cls.observable
        # if the record has anything to say
        if node.unresolved:
            # add it to the pile
            yield node.unresolved
        # my unresolved nodes know how to compute their values
        yield cls.unresolved
        # and whatever else my superclass says
        yield from cls.leafDerivation(node)
        # all done
        return


    # node probe
    @classmethod
    def probeDerivation(cls, node):
        """
        Build the {probe} base class sequence
        """
        # probes observe their operands
        yield cls.observer
        # they are themselves observable
        yield cls.observable
        # if the {node} has an opinion
        if node.probe:
            # add it to the pile
            yield node.probe
        # add the base class
        yield cls.probe
        # all done
        return


    # extended derivations of the user visible classes from my base class
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


    @classmethod
    def functionalDerivation(cls, func, node):
        """
        Create an operator whose evaluator is {func}
        """
        # functional nodes observe their operands
        yield from cls.observerDerivation(node)
        # and are themselves observable
        yield from cls.observableDerivation(node)
        # inject the evaluator
        yield func
        # and whatever else it takes to make a composite
        yield from cls.compositeDerivation(node)
        # all done
        return


# end of file
