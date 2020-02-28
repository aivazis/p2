# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclass
from ..patterns.Type import Type


# declaration
class Algebra(Type):
    """
    Metaclass that endows its instances with algebraic structure
    """


    # types
    # structural
    from .Leaf import Leaf as leaf
    from .Composite import Composite as composite
    # algebras
    from .Arithmetic import Arithmetic as arithmetic
    from .Ordering import Ordering as ordering
    from .Boolean import Boolean as boolean
    # the base node
    from .Node import Node as base
    # nodes
    from .Literal import Literal as literal
    from .Operator import Operator as operator
    from .Variable import Variable as variable


    # metamethods
    def __new__(cls, name, bases, attributes,
                arithmetic=True, ordering=False, boolean=False,
                basenode=False,
                **kwds):
        """
        Build a new class record
        """
        # if this is not the base node of the hierarchy
        if not basenode:
            # bypass any of my processing
            return super().__new__(cls, name, bases, attributes, **kwds)

        # prime the list of ancestors
        derivation = [cls.base]
        # add support for arithmetic, if requested
        if arithmetic: derivation.append(cls.arithmetic)
        # add support for ordering, if requested
        if ordering: derivation.append(cls.ordering)
        # add support for boolean operations, if requested
        if boolean: derivation.append(cls.boolean)
        # wrap up by piling on the actual bases of the client
        bases = tuple(derivation) + bases

        # build the record
        node = super().__new__(cls, name, bases, attributes, **kwds)

        # make literals
        node.literal = cls.make(name="literal", base=node, chain=cls.literalDerivation(node))
        # make variables
        node.variable = cls.make(name="variable", base=node, chain=cls.variableDerivation(node))
        # make operators
        node.operator = cls.make(name="operator", base=node, chain=cls.operatorDerivation(node))

        # return the record
        return node


    # implementation details
    # derivations of the user visible classes
    @classmethod
    def literalDerivation(cls, record):
        """
        Contribute to the list of ancestors of the representation of literals
        """
        # if the class record specifies a literal mix-in use it
        if record.literal: yield record.literal
        # must also derive from the default
        yield cls.literal
        # get the classes necessary to make leaves
        yield from cls.leafDerivation(record)
        # all done
        return


    @classmethod
    def operatorDerivation(cls, record):
        """
        Contribute to the list of ancestors of the representation of operators
        """
        # if the class record specifies a operator mix-in use it
        if record.operator: yield record.operator
        # must also derive from the default
        yield cls.operator
        # get the classes necessary to make composites
        yield from cls.compositeDerivation(record)
        # all done
        return


    @classmethod
    def variableDerivation(cls, record):
        """
        Contribute to the list of ancestors of the representation of variables
        """
        # if the class record specifies a variable mix-in use it
        if record.variable: yield record.variable
        # must also derive from the default
        yield cls.variable
        # get the classes necessary to make leaves
        yield from cls.leafDerivation(record)
        # all done
        return


    # structural contributions
    @classmethod
    def leafDerivation(cls, record):
        """
        Contribute to the list of ancestors of the representation of literals
        """
        # if the {record} specifies a leaf mix-in, add it to the pile
        if record.leaf: yield record.leaf
        # yield the default leaf class
        yield cls.leaf
        # and the buck stops here...
        yield record
        # all done
        return


    @classmethod
    def compositeDerivation(cls, record):
        """
        Contribute to the list of ancestors of the representation of literals
        """
        # if the {record} specifies a composite mix-in, add it to the pile
        if record.composite: yield record.composite
        # yield the default composite class
        yield cls.composite
        # and the buck stops here...
        yield record
        # all done
        return


    # record builder
    @classmethod
    def make(cls, name, base, chain):
        """
        Build a new class record to be attached to the node hierarchy
        """
        # realize the tuple of bases
        derivation = tuple(chain)
        # make the new class
        new = cls(name, derivation, {})
        # adjust its module so it get the correct attribution in stack traces
        new.__module__ = base.__module__
        # and return it
        return new


# end of file
