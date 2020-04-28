# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# externals
import collections    # for {defaultdict}
# framework
import p2             # for my superclass
# the palette definitions
from . import palettes


# the base class of journal devices
class Device(p2.patterns.named):
    """
    Base class for journal devices
    """


    # types
    from .Memo import Memo
    from .Alert import Alert


    # interface
    def alert(self, entry):
        """
        Generate an alert.

        Alerts are user-facing; they are generated by {info}, {warning}, and {error}
        """
        # invoke the alert renderer to format the message
        content = self.alertRenderer.render(palette=self.palette, entry=entry)
        # and record it
        self.record(page=content)
        # all done
        return self


    def memo(self, entry):
        """
        Issue a memo

        Memos are developer-facing; they are generated by {debug} and {firewall}
        """
        # invoke the memo renderer to format the message
        content = self.memoRenderer.render(palette=self.palette, entry=entry)
        # and record it
        self.record(page=content)
        # all done
        return self


    # metamethods
    def __init__(self, palette=palettes.null, alerts=None, memos=None, **kwds):
        # chain up
        super().__init__(**kwds)

        # save the renderers
        self.memoRenderer = memos if memos is not None else self.Memo()
        self.alertRenderer = alerts if alerts is not None else self.Alert()
        # save the palette
        self.palette = palette

        # all done
        return


    # implementation details
    def record(self, page):
        """
        Record a message
        """
        # this device doesn't know how to do that
        raise NotImplementedError(f"class '{type(self).__name__}' must implement 'record'")


# end of file
