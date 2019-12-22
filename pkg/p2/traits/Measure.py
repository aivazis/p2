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
        # figure out who the client is
        client = instance if instance is not None else cls
        # get its inventory; if the call came from a component instance, the inventory will be
        # an instance of {InstanceInventory}; otherwise, an instance of {ClassInventory}
        inventory = client.pyre_inventory
        # in either case, retrieve the value
        return inventory.getValue(component=client, trait=self)


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
        inventory.setValue(component=instance, trait=self, value=value,
                           locator=locator, priority=priority)
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
