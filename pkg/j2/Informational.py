# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# externals
import collections

# superclasses
from .Channel import Channel
from .Diagnostic import Diagnostic


# the implementation of the debug channel
class Informational(Diagnostic, Channel):
    """
    Informational channels are used for communicating application progress to users
    """


    # implementation details
    def commit(self):
        """
        Commit my payload to the journal
        """
        # if i'm not active
        if not self.state:
            # bail
            return self

        # otherwise, hunt down my device and record the entry
        self.device.alert(verbosity=self.verbosity, page=self.page, meta=self.meta)

        # all done
        return self


    # constant
    severity = "info" # the channel severity

    # my inventory type
    inventory_type = Channel.enabled_type
    # determines what my index holds
    index = collections.defaultdict(inventory_type)


# end of file
