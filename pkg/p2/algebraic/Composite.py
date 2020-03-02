# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


class Composite:
    """
    Mix-in class that provides an implementation of the subset of the interface of {Node} that
    requires traversal of the expression graph rooted at nodes with dependencies.

    This class assumes that its instances provide {operands}, a tuple of their dependencies on
    other nodes
    """


    # types
    from .exceptions import CircularReferenceError


    # interface
    @property
    def operands(self):
        """
        A sequence of my direct dependents
        """
        # the default implementation stores my operands in a private member
        return self._operands


    @property
    def span(self):
        """
        Return a sequence over my entire dependency graph
        """
        # i am a node in my dependency graph
        yield self
        # go through my operands
        for operand in self.operands:
            # and ask them for their span
            yield from operand.span
        # all done
        return


    # classifiers
    @property
    def literals(self):
        """
        Return a sequence over the nodes in my dependency graph that encapsulate foreign objects
        """
        # go through my operands
        for operand in self.operands:
            # and ask them for literals in their span
            yield from operand.literals
        # all done
        return


    @property
    def operators(self):
        """
        Return a sequence over the composite nodes in my dependency graph
        """
        # i am one
        yield self
        # go through my operands
        for operand in self.operands:
            # and ask them for operators in their span
            yield from operand.operators
        # all done
        return


    @property
    def variables(self):
        """
        Return a sequence over the variables in my dependency graph
        """
        # go through my operands
        for operand in self.operands:
            # and ask them for variables in their span
            yield from operand.variables
        # all done
        return


    # structural classifiers
    @property
    def leaves(self):
        """
        Return a sequence over the leaves in my dependency graph
        """
        # go through my operands:
        for operand in self.operands:
            # and ask them for leaves in their span
            yield from operand.leaves
        # all done
        return


    @property
    def composites(self):
        """
        Return a sequence over the composites in my dependency graph
        """
        # i am one
        yield self
        # go through my operands:
        for operand in self.operands:
            # and ask them for leaves in their span
            yield from operand.composites
        # all done
        return



    # alterations of the dependency graph
    def substitute(self, current, replacement, clean=None, isAcyclic=True):
        """
        Traverse my span and replace all occurrences of {current} with {replacement}

        This method makes it possible to introduce cycles in the dependency graph, which is not
        desirable typically. By default, we check that {self} is not in the span of
        {replacement}. Pass {isAcyclic=False} to bypass this check
        """
        # cycle detection
        if isAcyclic:
            # look for {self} in the span of {replacement}; do it carefully so
            # as not to trigger a call to the potentially overloaded {__eq__}, which may not
            # actually perform a comparison
            for node in replacement.span:
                # is this a match
                if node is self:
                    # the substitution would create a cycle
                    raise self.CircularReferenceError(node=self)

        # if the caller didn't hand me a pile of {clean} nodes
        if clean is None:
            # make a new one
            clean = set()
        # put {replacement} in the pile of {clean} nodes
        clean.add(replacement)

        # now, iterate over composites in my span
        for node in self.composites:
            # if this is a node we have visited before
            if node in clean:
                # skip it
                continue
            # otherwise, perform the substitution
            node._substitute(current=current, replacement=replacement)
            # and mark this node as clean
            clean.add(node)

        # all done
        return clean


    # metamethods
    def __init__(self, operands, **kwds):
        # chain up
        super().__init__(**kwds)
        # save my direct dependencies
        self._operands = tuple(operands)
        # all done
        return


    # implementation details
    def _substitute(self, current, replacement):
        """
        Adjust the operands by substituting {replacement} for {current} in the sequence of operands
        """
        # my new pile of operands
        operands = tuple(
            # consists of replacing {current} with {replacement} wherever i bump into it
            replacement if operand is current else operand
            # in the pile of dependencies
            for operand in self.operands
        )
        # attach the new pile
        self._operands = operands
        # all done
        return self


# end of file
