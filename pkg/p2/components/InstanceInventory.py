# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# support
from .. import tracking
from ..framework import priorities

# superclass
from .Inventory import Inventory


# declaration
class InstanceInventory(Inventory):
    """
    Storage for traits that belong to a component instance
    """


    # interface
    def getValue(self, component, trait):
        """
        Return the value associated with {trait}
        """
        # check whether i have a value for {trait}
        if trait in self:
            # in which case, return it
            return self[trait]

        # if not, this is the first time the value is requested AND the user hasn't provided a
        # value for this trait in a configuration event. we lookup the default value and add it
        # to this inventory

        # get the {component} class record
        cls = type(component)
        # get its inventory
        inventory = cls.pyre_inventory
        # ask it for the value
        value = inventory.getValue(component=cls, trait=trait)
        # build a locator
        locator = tracking.simple(f"default value")
        # set the assignment priority
        priority = priorities.Defaults()
        # associate {trait} with this value
        self.setValue(component=component, trait=trait, value=value,
                      priority=priority, locator=locator)

        # and return it
        return value


# end of file
