# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


class Simple:
    """
    A locator that records a simple named source with no further details
    """


    # meta methods
    def __init__(self, source):
        # record the source
        self.source = source
        # all done
        return


    def __str__(self):
        return str(self.source)


    # implementation details
    __slots__ = "source",


# end of file