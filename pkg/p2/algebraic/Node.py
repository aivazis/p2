# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# declaration
class Node:
    """
    The base class for hierarchies that implement the algebraic protocol

    The mix-in classes {Arithmetic}, {Ordering} and {Boolean} overload the methods that are
    invoked by the evaluation of expressions involving python operators. The implementation of
    these methods expect {Node} subclasses to provide access to two subclasses, {Literal} and
    {Operator}, that are used to build a representation of the python expression. {Literal} is
    used to encapsulate objects that are foreign to the {Node} class hierarchy, e.g. integers,
    and {Operation} encodes the operator encountered and its operands. This access must be
    provided through two {Node} properties, {literal} and {operation}, which provide an extra
    layer of abstraction by hiding the actual {Node} subclasses.
    """


    # exceptions; included here for client convenience
    from .exceptions import NodeError, CircularReferenceError


    # hooks for implementing the expression graph construction
    # structural
    leaf = None # nodes with no dependencies to other nodes
    composite = None # nodes with dependencies to other nodes
    # the node types
    literal = None # nodes that capture foreign values
    variable = None # the base class of my native nodes
    operator = None # operations among my native nodes


    # interface
    # graph traversal
    @property
    def operands(self):
        """
        A sequence of my direct dependents
        """
        # by default, empty
        return ()


    @property
    def span(self):
        """
        A sequence over my entire dependency graph
        """
        # by default, empty
        return ()


    # node classifiers
    @property
    def literals(self):
        """
        A sequence over the nodes in my dependency graph that encapsulate foreign objects
        """
        # by default, empty
        return ()


    @property
    def operators(self):
        """
        A sequence over the composite nodes in my dependency graph
        """
        # by default, empty
        return ()


    @property
    def variables(self):
        """
        A sequence over the leaf nodes in my dependency graph
        """
        # by default, empty
        return ()


    # structural classifiers
    @property
    def leaves(self):
        """
        Return a sequence over the leaves in my dependency graph
        """
        # by default empty
        return ()


    @property
    def composites(self):
        """
        Return a sequence over the composites in my dependency graph
        """
        # by default, empty
        return ()


    # interface
    def isCyclic(self):
        """
        Determine whether my subgraph has any cycles
        """
        # initialize my markers
        known = set()
        # go through my span
        for node in self.span:
            # if i've seen it before
            if node in known:
                # it's a cycle
                return node
            # add this to the pile and move on
            known.add(node)
        # no cycles were detected
        return None


    def replace(self, obsolete):
        """
        Take ownership of any information held by the {obsolete} node, which is about to be
        destroyed
        """
        # i don't know how to do that; my subclasses might
        return self


# end of file
