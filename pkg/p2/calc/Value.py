# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# value management
class Value:
    """
    Mix-in class that provides storage for a node value
    """


    # interface
    def getValue(self):
        """
        Return my value
        """
        # easy enough
        return self._value


    def setValue(self, value):
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
        self._value = self.initialize(value=value)
        # all done
        return


    # implementation details
    def initialize(self, value):
        """
        Invoked by the constructor to prep the initial value of the node
        """
        # the default implementation is to leave the value alone
        return value


    # private data
    _value = None


# end of file
