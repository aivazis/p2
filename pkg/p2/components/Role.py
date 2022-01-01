# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# support
from .. import tracking

# superclass
from .Requirement import Requirement


# declaration
class Role(Requirement):
    """
    The metaclass for protocols
    """


    # metamethods
    def __new__(cls, name, bases, attributes, **kwds):
        """
        Build a new protocol class record
        """
        # chain up
        protocol = super().__new__(cls, name, bases, attributes, **kwds)
        # save the location of the protocol declaration
        protocol.pyre_locator = tracking.here(level=1)
        # all done
        return protocol


    def __init__(self, name, bases, attributes, **kwds):
        """
        Initialize a freshly minted protocol record
        """
        # chain up
        super().__init__(name, bases, attributes, **kwds)

        # registration
        # get the dashboard
        from .. import dashboard
        # get the registrar
        registrar = dashboard.registrar
        # ask it to register this component class
        registrar.registerProtocolClass(protocol=self)
        # and invoke the registration hook
        self.pyre_classRegistered()

        # class configuration is now complete
        self.pyre_classConfigured()
        # so is initialization
        self.pyre_classInitialized()

        # all done
        return


    def __str__(self):
        """
        Build a human readable representation
        """
        # use my family name
        marker = self.pyre_family
        # if i don't have one
        if marker is None:
            # use my class name
            marker = self.__name__
        # build the rep and return it
        return f"protocol '{marker}'"


# end of file
