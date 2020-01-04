# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# factories
def newPathHash(**kwds):
    """
    Build a hashing functor for hierarchical name spaces
    """
    # get the factory
    from .PathHash import PathHash
    # and invokei t
    return PathHash(**kwds)


# end of file
