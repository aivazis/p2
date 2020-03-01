# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


class Leaf:
    """
    Mix-in class that provides an implementation of the subset of the interface of {Node} that
    requires traversals of the expression graph rooted at leaf nodes.
    """


    # interface
    @property
    def span(self):
        """
        Traverse my subgraph and yield all its nodes
        """
        # just myself
        yield self
        # and nothing else
        return


    # structural classifiers
    @property
    def leaves(self):
        """
        Return a sequence over the leaves in my dependency graph
        """
        # i am one
        yield self
        # all done
        return


# end of file
