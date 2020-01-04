# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclass
from .Requirement import Requirement


# declaration
class Role(Requirement):
    """
    The metaclass for protocols
    """


    # metamethods
    def __str__(self):
        """
        Build a human readable representation
        """
        # use my family name
        marker = self.pyre_family
        # if i don't have one
        if marker is None:
            # use my class name
            marker = self.__name__
        # build the rep and return it
        return f"protocol '{marker}'"


# end of file
