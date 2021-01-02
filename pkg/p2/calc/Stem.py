# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# superclass
from ..algebraic.Node import Node


# augmented base node
class Stem(Node):
    """
    The base class for nodes that have values
    """


    # types
    # augmented structural nodes
    from .Composite import Composite as composite

    # new composites
    expression = None
    interpolation = None
    reference = None
    unresolved = None

    # containers
    # sequences and realizations
    sequence = None
    list = None
    set = None
    tuple = None
    # mappings and realizations
    mapping = None
    dict = None

    # node probes
    probe = None

    # exceptions; included here for client convenience
    from .exceptions import (
        EmptyExpressionError, ExpressionSyntaxError, EvaluationError,
        UnresolvedNodeError
        )


    # public data
    @property
    def value(self):
        """
        Get my value
        """
        # attempt to
        try:
            # ask me for my value
            return self.getValue()
        # if reading is not supported
        except AttributeError:
            # complain
            raise self.EvaluationError(node=self, error="node value is not readable")


    @value.setter
    def value(self, value):
        """
        Set my value
        """
        # attempt to
        try:
            # set my value
            return self.setValue(value=value)
        # if writing is not supported
        except AttributeError:
            # complain
            raise self.EvaluationError(node=self, error="node value is not writable")


    # classifiers
    @property
    def expressions(self):
        """
        Return a sequence over the nodes in my dependency graph that are constructed out of python
        expressions involving the names of other nodes
        """
        # by default, empty
        return ()


    @property
    def interpolations(self):
        """
        Return a sequence over the nodes in my dependency graph that are constructed by expanding
        the values of other nodes in a macro
        """
        # by default, empty
        return ()


    @property
    def mappings(self):
        """
        Return a sequence over the nodes in my dependency graph that are mappings
        """
        # by default, empty
        return ()


    @property
    def references(self):
        """
        Return a sequence over the nodes in my dependency graph that are references to other nodes
        """
        # by default, empty
        return ()


    @property
    def sequences(self):
        """
        Return a sequence over the nodes in my dependency graph that are sequences
        """
        # by default, empty
        return ()


    @property
    def unresolveds(self):
        """
        Return a sequence over the nodes in my dependency graph that represent requests for model
        names that don't exist
        """
        # by default, empty
        return ()


    # interface
    def ref(self, **kwds):
        """
        Build and return a reference to me
        """
        # use the class factory to make one and return it
        return self.reference(operands=(self,), **kwds)


# end of file
