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
    # algebraic
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
                arithmetic=True, ordering=True, boolean=True,
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
        record = super().__new__(cls, name, bases, attributes, **kwds)

        # build the list of base classes for the literal
        derivation = tuple(cls.literalDerivation(record))
        # make one
        record.literal = cls('literal', derivation, {})
        # adjust its module so it gets the correct attribution in stack traces
        record.literal.__module__ = record.__module__

        # build the list of base classes for the variable
        derivation = tuple(cls.variableDerivation(record))
        # make one
        record.variable = cls('variable', derivation, {})
        # adjust its module so it gets the correct attribution in stack traces
        record.variable.__module__ = record.__module__

        # build the list of base classes for operators
        derivation = tuple(cls.operatorDerivation(record))
        # make one
        record.operator = cls('operator', derivation, {})
        # adjust its module so it gets the correct attribution in stack traces
        record.operator.__module__ = record.__module__

        # return the record
        return record


    # implementation details
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


# end of file
