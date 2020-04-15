# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# for my metaclass
import p2


# the singleton that owns the global state
class Chronicler(metaclass=p2.patterns.singleton):
    """
    The manager of the journal global state
    """


    # public data
    device = None


    # metamethods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)

        # the default verbosity
        self.verbosity = 1
        # the default device
        self.device = None
        # the global metadata
        self.meta = {
            "application": "journal",  # this key is required; applications should override
            }

        # all done
        return


# end of file
