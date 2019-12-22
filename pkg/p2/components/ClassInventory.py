# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# superclass
from .Inventory import Inventory


# declaration
class ClassInventory(Inventory):
    """
    Storage for traits that belong to a component class record
    """


    # interface
    def getValue(self, component, trait):
        """
        Return the value associated with {trait}
        """
        # {component} is expected to be the owner of this inventory. the strategy here is to
        # walk up the {mro} looking for a class whose inventory contains a value for {trait};
        # if we hit the class that originally declared this trait, we terminate the look up and
        # return the default values stored with the trait. it is true that the first lookup
        # through the {mro} returns this inventory, but the code seems simpler this way

        # get the class that declared this {trait}
        origin = trait.origin
        # go through the {mro} of {component}
        for link in component.pyre_pedigree:
            # get the inventory of this ancestor
            inventory = link.pyre_inventory
            # if there is a value for this {trait} here
            if trait in inventory:
                # get it and return it
                return inventory[trait]
            # if we have arrived at the class that originally declared this {trait}
            if link is origin:
                # nobody has a value for this trait; hand over its default value
                return trait.default

        # if we exhausted the search without finding a value, we have a bug
        import journal
        # make a channel
        channel = journal.firewall("pyre.traits")
        # build an error report
        msg = f"could not find a value for '{trait.name}' in {component}"
        # and complain
        raise channel.log(message)


# end of file
