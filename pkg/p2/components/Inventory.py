# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# declaration
class Inventory:
    """
    Storage for component traits
    """


    # public data
    traits = None # the table of trait values


    # interface
    def getValue(self, component, trait):
        """
        Return the value associated with {trait}
        """
        # look it up in my table of values
        return self[trait]


    def setValue(self, component, trait, value, locator, priority):
        """
        Set the {value} of this {trait}
        """
        # place in my table of values
        self[trait] = value
        # all done
        return


    def deleteValue(self, trait):
        """
        Remove the value associated with {trait}
        """
        # remove form my table of values
        del self[trait]
        # all done
        return


    # metamethods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # initialize my table of values
        self.traits = {}
        # all done
        return


    # avoid using these directly as they require knowledge of the actual objects used to store
    # the trait values, something that should be treated as an implementation detail. use the
    # high level interface instead, after checking with a component that the {trait} you are
    # looking for is one it knows

    def __contains__(self, item):
        # ask my table
        return item in self.traits


    def __iter__(self):
        # iterate over the keys in my table of values
        return iter(self.traits)


    def __delitem__(self, trait):
        # delegate
        del self.traits[trait]
        # all done
        return


    def __getitem__(self, trait):
        # delegate
        return self.traits[trait]


    def __setitem__(self, trait, value):
        # delegate
        self.traits[trait] = value
        # all done
        return


# end of file
