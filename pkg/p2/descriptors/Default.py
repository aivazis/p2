# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# declaration
class Default:
    """
    Mix-in class that endows descriptors with the ability to manage a default value
    """


    # public data
    # the default value
    default = None


    # meta-methods
    def __init__(self, default=default, **kwds):
        # chain up
        super().__init__(**kwds)
        # record the name
        self.default = default
        # all done
        return


# end of file
