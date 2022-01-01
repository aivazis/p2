# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# mix-in for building classes that have a public name
class Named:
    """
    Keeper of the name
    """


    # public data
    @property
    def name(self):
        """
        Get my name
        """
        # easy enough
        return self._name


    # metamethods
    def __init__(self, name, **kwds):
        # chain up
        super().__init__(**kwds)
        # store the name
        self._name = name
        # all done
        return


    # implementation details
    _name = None  # storage for the {name} property


# end of file
