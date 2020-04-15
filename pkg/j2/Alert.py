# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclass
from .Renderer import Renderer


# the renderer or user-facing essages
class Alert(Renderer):
    """
    The renderer of user-facing messages
    """


    # implementation details
    def header(self, palette, page, meta):
        """
        Generate the message header
        """
        # if there's nothing to do
        if not page:
            # bail
            return

        # get the severity
        severity = meta["severity"]
        # generate
        buffer = [
            palette[severity], meta["application"], palette["reset"],
            "(",
            palette[severity], severity, palette["reset"],
            "): ",
            palette["body"], page[0], palette["reset"]
            ]
        # assemble and push
        yield ''.join(buffer)

        # all done
        return


    def body(self, palette, page, meta):
        """
        Generate the message body
        """
        # if there's nothing to do
        if len(page) < 2:
            # bail
            return

        # otherwise, go through the page contents
        for line in page[1:]:
            # make a buffer
            buffer = [
                palette["body"], line, palette["reset"]
                ]
            # assemble and push
            yield ''.join(buffer)

        # all done
        return


# end of file
