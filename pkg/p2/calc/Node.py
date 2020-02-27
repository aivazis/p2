# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# metaclass
from . import calculator


# the anchor class for lazily evaluated nodes
class Node(metaclass=calculator, basenode=True):
    """
    The base node for lazily evaluated node graphs
    """


# end of file
