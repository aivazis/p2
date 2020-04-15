# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# the base exception from the framework
from p2.framework.exceptions import PyreError


# all local exceptions derive from this
class JournalError(PyreError):
    """
    Base class for all journal errors

    Useful when you are trying to catch all journal errors
    """


# raised by firewalls
class FirewallError(JournalError):
    """
    Exception raised when firewalls fire
    """

    # public data
    description = "firewall breached; aborting..."

    # metamethods
    def __init__(self, firewall, **kwds):
        # chain up
        super().__init__(locator=firewall.locator, **kwds)
        # save the firewall
        self.firewall = firewall
        # all done
        return


# raise by error channels
class ApplicationError(JournalError):
    """
    Exception raised when an application error is encountered
    """

    # public data
    description = "application error; aborting..."

    # metamethods
    def __init__(self, error, **kwds):
        # chain up
        super().__init__(locator=error.locator, **kwds)
        # save the firewall
        self.error = error
        # all done
        return


# end of file
