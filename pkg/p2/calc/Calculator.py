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


    # meta methods
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


    # implementation details
    @classmethod
    def expressionDerivation(cls, record):
        """
        Contribute to the list of ancestors of the representation of expressions
        """
        # make a managed dependent
        yield from cls.managedDependentDerivation()
        # if the record has anything to contribute
        if record.expression:
            # this is its spot
            yield record.expression
        # the local base with the default behavior
        yield cls.expression
        # and whatever else it takes to represent a composite
        yield from cls.compositeDerivation(record)
        # all done
        return


    # hierarchy fragments
    @classmethod
    def managedDependencyDerivation(cls):
        """
        Base classes for making a node record that other nodes can depend on
        """
        # my local nodes memoize their values
        yield cls.memo
        # support arbitrary value conversions
        yield cls.preprocessor
        yield cls.postprocessor
        # notify their clients of changes to their values
        yield cls.dependency
        yield cls.observable
        # all done
        return


    @classmethod
    def managedDependentDerivation(cls):
        """
        Base classes for making a node record that can depend on other nodes
        """
        # my local nodes memoize their values
        yield cls.memo
        # support arbitrary value conversions
        yield cls.preprocessor
        yield cls.postprocessor
        # notify their clients of changes to their values and respond when the values of their
        # operands change
        yield cls.dependent
        yield cls.observer
        yield cls.dependency
        yield cls.observable
        # all done
        return





# end of file
