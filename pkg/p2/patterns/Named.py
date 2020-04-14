# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# mix-in for building classes that have a public name
class Named:
    """
    Keeper of the name
    """


    # public data
    name = None


    # metamethods
    def __init__(self, name, **kwds):
        # chain up
        super().__init__(**kwds)
        # store the name
        self.name = name
        # all done
        return


# end of file
