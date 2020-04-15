# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# externals
import collections    # for {defaultdict}
# framework
import p2             # for my superclass
# access to the global settings
from .Chronicler import Chronicler


# the base class of journal devices
class Device(p2.patterns.named):
    """
    Base class for journal devices
    """


    # types
    from .Memo import Memo
    from .Alert import Alert


    # class data
    # access to the singleton with the global journal configuration
    chronicler = Chronicler()


    # interface
    def alert(self, verbosity, page, meta):
        """
        Generate an alert.

        Alerts are user-facing; they are generated by {info}, {warning}, and {error}
        """
        # get the verbosity level
        maxVerbosity = self.chronicler.verbosity
        # if this commit exceeds that
        if verbosity > maxVerbosity:
            # nothing to do
            return self
        # otherwise, invoke the alert renderer to format the message
        content = self.alertRenderer.render(palette=self.palette, page=page, meta=meta)
        # ask the subclass to record
        self.record(message=content)
        # all done
        return self


    def memo(self, verbosity, page, meta):
        """
        Issue a memo

        Memos are developer-facing; they are generated by {debug} and {firewall}
        """
        # get the verbosity level
        maxVerbosity = self.chronicler.verbosity
        # if this commit exceeds that
        if verbosity > maxVerbosity:
            # nothing to do
            return self
        # otherwise, invoke the alert renderer to format the message
        content = self.memoRenderer.render(palette=self.palette, page=page, meta=meta)
        # ask the subclass to record
        self.record(message=content)
        # all done
        return self


    # metamethods
    def __init__(self, palette=None, alerts=None, memos=None, **kwds):
        # chain up
        super().__init__(**kwds)

        # save the renderers
        self.memoRenderer = memos if memos is not None else self.Memo()
        self.alertRenderer = alerts if alerts is not None else self.Alert()
        # save the palette
        self.palette = collections.defaultdict(str) if palette is None else palette

        # all done
        return


    # implementation details
    def record(self, message):
        """
        Record a message
        """
        # this device doesn't know how to do that
        raise NotImplementedError(f"class '{type(self).__name__}' must implement 'record'")


# end of file
