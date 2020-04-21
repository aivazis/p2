# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclasses
from .Channel import Channel
from .Diagnostic import Diagnostic


# the implementation of the debug channel
class Error(Diagnostic, Channel, inventory_type=Channel.enabled_fatal_type):
    """
    Error channels are used for communicating application progress to users
    """


    # interface
    @property
    def fatal(self):
        """
        Check whether i'm fatal
        """
        # my inventory knows
        return self.inventory.fatal


    @fatal.setter
    def fatal(self, flag):
        """
        Set whether i'm fatal
        """
        # pass the flag to my inventory
        self.inventory.fatal = flag
        # all done
        return


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
    severity = "error" # the channel severity


# end of file