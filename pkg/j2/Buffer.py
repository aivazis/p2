# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# content accumulator
class Buffer:
    """
    Accumulator of content and metadata for journal messages
    """


    # public data
    page = None # a list of lines of output
    meta = None # a dictionary with the message metadata


    # metamethods
    def __init__(self, meta, **kwds):
        # chain up
        super().__init__(**kwds)
        # start with a blank page
        self.page =  []
        # and a copy of the supplied metadata
        self.meta = dict(meta)
        # all done
        return


# end of file
