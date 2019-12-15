# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


class NameLookup:
    """
    A locator that records a simple named source with no further details
    """


    # meta methods
    def __init__(self, description, key):
        # record the look up key and a description
        self.key = key
        self.description = description
        # all done
        return


    def __str__(self):
        # get access to the framework managers
        from ..framework.Dashboard import Dashboard
        # get the nameserver
        ns = Dashboard.pyre_nameserver
        # generate my rep
        return f"{self.description} {ns[self.key]}"


    # implementation details
    __slots__ = "key", "description"


# end of file
