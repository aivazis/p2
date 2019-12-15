# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# support
from .. import tracking

# superclass
from .Requirement import Requirement


# declaration
class Actor(Requirement):
    """
    The metaclass of components

    {Actor} takes care of all the tasks necessary to convert a component declaration into a
    configurable entity that coöperates fully with the framework
    """


    # types
    from .Role import Role
    from .Inventory import Inventory


    # metamethods
    def __new__(cls, name, bases, attributes, *, family=None, implements=None, **kwds):
        """
        Build a new component record
        """
        # chain up; swallow the locally specified keywords
        component = super().__new__(cls, name, bases, attributes, **kwds)

        # build the protocol specification
        component.pyre_protocol = cls.pyre_buildProtocol(component=component, implements=implements)
        # save the location of the component declaration
        component.pyre_locator = tracking.here(level=1)

        # all done
        return component


    def __init__(self, name, bases, attributes, *, family=None, implements=None, **kwds):
        """
        Initialize a freshly minted component record
        """
        # chain up
        super().__init__(name, bases, attributes, **kwds)

        # if this is an internal component
        if self.pyre_isInternal:
            # there is nothing further to do
            return

        # build the class inventory
        self.pyre_inventory = self.Inventory()

        # all done
        return


    # implementation details
    @classmethod
    def pyre_buildProtocol(cls, component, implements):
        """
        Build a class that describes the implementation requirements imposed on the {component}
        under construction
        """
        # NYI
        protocols = ()
        # make one and return it
        return cls.Role("protocol", protocols, {}, internal=True)


# end of file
