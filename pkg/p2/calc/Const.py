# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# declaration
class Const:
    """
    Mix-in class that serves a read-only value that must be set during construction
    """

    # value management
    def getValue(self):
        """
        Return my value
        """
        # easy enough
        return self._value


    def setValue(self, value):
        """
        Disable value setting
        """
        # disabled
        raise NotImplementedError("const nodes do not support 'setValue'")


# end of file
