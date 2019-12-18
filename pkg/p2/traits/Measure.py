# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# support
from .. import tracking
from ..framework import priorities

# superclasses
from .Trait import Trait
# mixins
from ..descriptors.Default import Default
from ..descriptors.DataDescriptor import DataDescriptor


# declaration
class Measure(Trait, Default, DataDescriptor):
    """
    The base class of all traits that require storage for user configurable state
    """


    # framework data
    category = 'measure'
    # predicate that indicates whether this trait is subject to runtime configuration
    isMeasure = True


    # metamethods
    def __get__(self, instance, cls):
        """
        Retrieve the value of this trait
        """
        # if the request came from an actual instance
        if instance is not None:
            # grab its inventory
            inventory = instance.pyre_inventory
            # if there is a value for me
            if self in inventory:
                # return it
                return inventory.getValue(trait=self)

        # get the class that declared me
        origin = self.origin
        # if i couldn't find a value in the instance inventory, or if this request came from a
        # component class, we must go through the {mro} of the class looking through the
        # inventories for ancestor components that might have a value
        for link in cls.pyre_pedigree:
            # get the inventory of this ancestor
            inventory = link.pyre_inventory
            # if there is a value for me here
            if self in inventory:
                # get it and return it
                return inventory.getValue(trait=self)
            # if we have arrived at the class that declared me
            if link is origin:
                # nobody has a value for me; hand my default value
                return self.default

        # if we exhausted the search through the ancestors without finding a value, we have a bug
        import journal
        # make a channel
        channel = journal.firewall("pyre.traits")
        # build an error report
        msg = f"could not find a value for '{self.name}' in {cls}"
        # and complain
        raise channel.log(msg)


    def __set__(self, instance, value):
        """
        Set the value of this trait
        """
        # build a locator
        locator = tracking.here(level=1)
        # set the priority of this assignment
        priority = priorities.Explicit()
        # get the inventory
        inventory = instance.pyre_inventory
        # set the value
        inventory.setValue(trait=self, value=value, locator=locator, priority=priority)
        # all done
        return


    def __delete__(self, instance):
        """
        Delete the value of this trait in {instance}
        """
        # get the inventory
        inventory = instance.pyre_inventory
        # delete the value
        inventory.deleteValue(trait=self)
        # all done
        return


# end of file
