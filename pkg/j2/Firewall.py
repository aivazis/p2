# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclasses
from .Channel import Channel
from .Diagnostic import Diagnostic


# the implementation of the Firewall channel
class Firewall(Diagnostic, Channel, inventory_type=Channel.enabled_fatal_type):
    """
    Debug channels are used for communicating application progress to its developers
    """


    # types
    from .exceptions import FirewallError


    # public data
    @property
    def fatal(self):
        # ask my inventory
        return self.inventory.fatal


    @fatal.setter
    def fatal(self, flag):
        # set my inventory
        self.inventory.fatal = flag
        # all done
        return


    # implementation details
    def commit(self):
        """
        Commit my payload to the journal
        """
        # if i'm active
        if self.state:
            #  hunt down my device and record the entry
            self.device.memo(verbosity=self.verbosity, page=self.page, meta=self.meta)

        # if i'm fatal
        if self.fatal:
            # generate an exception
            raise self.FirewallError(firewall=self)

        # all done
        return self


    # constant
    severity = "firewall"     # the channel severity


# end of file