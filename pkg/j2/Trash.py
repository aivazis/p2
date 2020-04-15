# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclass
from .Device import Device


# swallow all requests to record a message
class Trash(Device):
    """
    Journal device that ignores all requests to write a message
    """

    # constants
    name = "trash"


    # metamethods
    def __init__(self, name=name,  **kwds):
        # chain up
        super().__init__(name=name, **kwds)
        # all done
        return


    # implementation details
    def record(self, message):
        """
        Record a message
        """
        # do nothing
        return self


# end of file
