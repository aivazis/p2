# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# superclass
from .Configurable import Configurable


# declaration
class Facility(Configurable):
    """
    The base class for traits that are components
    """


    # framework data
    category = 'facility'
    # predicate that indicates whether this trait holds a component
    isFacility = True


# end of file
