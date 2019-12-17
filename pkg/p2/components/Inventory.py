# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# declaration
class Inventory:
    """
    Storage for component traits
    """


    # public data
    traits = None


    # interface
    def getValue(self, trait):
        """
        Return the value associated with {trait}
        """
        # delegate
        return self.traits[trait]


    def setValue(self, trait, value, locator, priority):
        """
        Set the {value} of this {trait}
        """
        # delegate
        self.traits[trait] = value
        # all done
        return


    def deleteValue(self, trait):
        """
        Remove the value associated with {trait}
        """
        # delegate
        del self.traits[trait]
        # all done
        return


    # metamethods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # initialize my table
        self.traits = {}
        # all done
        return


    def __contains__(self, item):
        # delegate to my table
        return item in self.traits


    def __iter__(self):
        # delegate
        return iter(self.traits)


# end of file
