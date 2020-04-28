# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# content accumulator
class Entry:
    """
    Accumulator of content and metadata for journal messages
    """


    # public data
    page = None  # a list of lines of output
    notes = None # a dictionary with the message metadata


    # metamethods
    def __init__(self, notes, **kwds):
        # chain up
        super().__init__(**kwds)
        # start with a blank page
        self.page =  []
        # and a copy of the supplied metadata
        self.notes = dict(notes)
        # all done
        return


    def __iter__(self):
        """
        Support for quick unpacking
        """
        # make a tuple and hand it off
        return self.page, self.notes


# end of file
