# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# a placeholder for nodes that have been referenced but are not yet defined
class Unresolved:
    """
    A node that raises {UnresolvedNodeError} when its value is read
    """


    # exceptions
    from .exceptions import UnresolvedNodeError


    # constants
    category = 'unresolved'
    # public data
    request = None # the unresolved name


    # classifiers
    @property
    def unresolveds(self):
        """
        Return a sequence over the unresolved nodes in my dependency graph
        """
        # i am one
        yield self
        # nothing further
        return


    # value management
    def getValue(self):
        """
        Compute my value
        """
        # asking for my value is an error
        raise self.UnresolvedNodeError(node=self, name=self.request)


    # support for graph traversals
    def identify(self, authority, **kwds):
        """
        Let {authority} know I am an unresolved node
        """
        # invoke the callback
        return authority.onUnresolved(unresolved=self, **kwds)


    # meta methods
    def __init__(self, request, **kwds):
        # chain up
        super().__init__(**kwds)
        # store the name of the requested node
        self.request = request
        # all done
        return


    def __str__(self):
        # i have a name...
        return self.request


    # debugging support
    def dump(self, name, indent):
        print(f"{indent}{name}: <unresolved>")
        return self


# end of file
