# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclass
from .Device import Device


# write message to a stream
class Stream(Device):
    """
    Journal device that writes messages to a stream
    """


    # interface
    def close(self):
        """
        Close the associated stream
        """
        # delegate
        self.stream.close()
        # all done
        return self


    # metamethods
    def __init__(self, stream, name="stream", **kwds):
        # chain up
        super().__init__(name=name, **kwds)
        # save the stream
        self.stream = stream
        # all done
        return


    # implementation details
    def record(self, page):
        """
        Record a message
        """
        # assemble the content
        content = "\n".join(page)
        # if there is anything there
        if content:
            # inject it
            print(content, file=self.stream)
        # all done
        return


# end of file
