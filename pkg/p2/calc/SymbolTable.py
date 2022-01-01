# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# a mapping of names to nodes
class SymbolTable:
    """
    Storage and naming services for {calc} nodes
    """


    # types
    from .Node import Node as node

    # exceptions; included here for client convenience
    from .exceptions import (
        NodeError,
        CircularReferenceError,
        EmptyExpressionError, ExpressionSyntaxError, EvaluationError,
        UnresolvedNodeError
        )


    # interface
    def keys(self):
        """
        Build a sequence of my registered keys
        """
        # delegate to my map
        yield from self._nodes.keys()
        # all done
        return


    def nodes(self):
        """
        Build a sequence of my registered nodes
        """
        # delegate to my map
        yield from self._nodes.values()
        # all done
        return


    def insert(self, name, node):
        """
        Insert {node} in the symbol table under {name}. If there is an existing node, adjust the
        evaluation graph by replacing the existing node with the new one everywhere
        """
        # look for
        try:
            # an existing one
            old = self._nodes[name]
        # if not there
        except KeyError:
            # no problem; just remember
            old = None
        # if there is an existing node
        else:
            # replace it
            node.replace(old)

        # update the model
        self._nodes[name] = node

        # and return
        return name, node, old


    def resolve(self, name):
        """
        Retrieve the node registered under {name}. If no such node exists, an error marker will
        be built, stored in the symbol table under {name}, and returned.
        """
        # if a node is already registered under {name}
        try:
            # grab it
            node = self._nodes[name]
        # otherwise
        except KeyError:
            # build an error marker
            node = self.node.unresolved(request=name)
            # add it to the pile
            self._nodes[name] = node
        # and return it
        return node


    # convenience: node constructors
    def dict(self, value, name=None, **kwds):
        """
        Build a mapping node
        """
        # make the node
        new = self.node.dict(value=value, **kwds)
        # if we were given a name
        if name is not None:
            # add the node to the table
            self.insert(name=name, node=new)
        # and return the new node
        return new


    def expression(self, value, name=None, **kwds):
        """
        Build an expression node
        """
        # if the value is already a node
        if isinstance(value, self.node):
            # just return it
            return value
        # if it is not a string
        if not isinstance(value, str):
            # just make a variable
            return self.variable(name=name, value=value, **kwds)
        # otherwise, attempt to
        try:
            # compile the {value}
            program, operands = self.node.expression.compile(model=self, expression=value)
        # if this fails
        except self.node.EmptyExpressionError as error:
            # make a variable instead; use the processed value to get rid of the meta-characters
            return self.variable(name=name, value=error.normalized, **kwds)

        # if all is well, build an expression
        new = self.node.expression(model=self, expression=value,
                                   program=program, operands=operands, **kwds)
        # if we were given a name
        if name is not None:
            # insert the node in the table
            self.insert(name=name, node=new)

        # and return the new node
        return new


    def interpolation(self, value, name=None, **kwds):
        """
        Build an interpolation node
        """
        # if the value is already a node
        if isinstance(value, self.node):
            # just return it
            return value
        # if it is not a string
        if not isinstance(value, str):
            # just make a variable
            return self.variable(name=name, value=value, **kwds)
        # otherwise, attempt to
        try:
            # compile the {value}
            operands = self.node.interpolation.compile(model=self, expression=value)
        # if this fails
        except self.node.EmptyExpressionError as error:
            # make a variable instead; use the processed value to get rid of the meta-characters
            return self.variable(name=name, value=error.normalized, **kwds)

        # if all is well, build an interpolation
        new = self.node.interpolation(model=self, expression=value,
                                      operands=operands, **kwds)
        # if we were given a name
        if name is not None:
            # add the node to the table
            self.insert(name=name, node=new)

        # and return the new node
        return new


    def list(self, value, name=None, **kwds):
        """
        Build a sequence node
        """
        # make the node
        new = self.node.list(value=value, **kwds)
        # if we were given a name
        if name is not None:
            # add the node to the table
            self.insert(name=name, node=new)
        # and return the new node
        return new


    def literal(self, **kwds):
        """
        Build a literal node
        """
        # easy enough
        return self.node.literal(**kwds)


    def set(self, value, name=None, **kwds):
        """
        Build a sequence node
        """
        # make the node
        new = self.node.set(value=value, **kwds)
        # if we were given a name
        if name is not None:
            # add the node to the table
            self.insert(name=name, node=new)
        # and return the new node
        return new


    def tuple(self, value, name=None, **kwds):
        """
        Build a sequence node
        """
        # make the node
        new = self.node.tuple(value=value, **kwds)
        # if we were given a name
        if name is not None:
            # add the node to the table
            self.insert(name=name, node=new)
        # and return the new node
        return new


    def variable(self, name=None, **kwds):
        """
        Build a variable
        """
        # make the node
        new = self.node.variable(**kwds)
        # if we were given a name
        if name is not None:
            # add the node to the table
            self.insert(name=name, node=new)
        # and return the new node
        return new


    # meta-methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # initialize my node map
        self._nodes = {}
        # all done
        return


    def __contains__(self, name):
        """
        Check whether {name} is present in the symbol table
        """
        # check whether it is present in my node index
        return name in self._nodes


    def __iter__(self):
        """
        Go through my keys
        """
        # easy enough
        return iter(self._nodes)


    def __getitem__(self, name):
        """
        Look up the node registered under {name} and return its value
        """
        # get the node
        node = self.resolve(name)
        # compute and return its value
        return node.getValue()


    def __setitem__(self, name, value):
        """
        Add or update the named node with the given {value}
        """
        # convert {value} into an appropriate node; this relies on {interpolation} passing
        # through any value that is a node, and constructing variables for non-string values
        # and empty expressions
        new = self.interpolation(value=value)
        # insert it into the model and return
        return self.insert(node=new, name=name)


    # private data
    _nodes = None


# end of file
