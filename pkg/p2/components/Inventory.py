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


    def __getitem__(self, trait):
        # delegate
        return self.traits[trait]


    def __setitem__(self, trait, item):
        # delegate
        self.traits[trait] = item
        # all done
        return

    def __delitem__(self, item):
        # delegate
        del self.traits[trait]
        # all done
        return


# end of file
