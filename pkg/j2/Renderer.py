# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# the base renderer
class Renderer:
    """
    The base renderer
    """


    # interface
    def render(self, palette, page, meta):
        """
        Generate the message content
        """
        # each rendered message has three sections
        yield from self.header(palette=palette, page=page, meta=meta)
        yield from self.body(palette=palette, page=page, meta=meta)
        yield from self.footer(palette=palette, page=page, meta=meta)

        # all done
        return


    # implementation details
    def header(self, **kwds):
        """
        Generate the message header
        """
        # nothing to do
        return ()


    def body(self, **kwds):
        """
        Generate the message body
        """
        # nothing to do
        return ()


    def footer(self, **kwds):
        """
        Generate the message footer
        """
        # nothing to do
        return ()


# end of file
