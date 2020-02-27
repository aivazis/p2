# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# value management
class Value:
    """
    Mix-in class that provides storage for a node value
    """


    # interface
    def getValue(self, **kwds):
        """
        Return my value
        """
        # easy enough
        return self._value


    def setValue(self, **kwds):
        """
        Set my value
        """
        # store
        self._value = value
        # all done
        return


    # metamethods
    def __init__(self, value, **kwds):
        # chain up
        super().__init__(**kwds)
        # save the value
        self.setValue(value=value)
        # all done
        return


    # private data
    _value = None


# end of file
