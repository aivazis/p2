# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# superclass
from .Measure import Measure


# declaration
class Facility(Measure):
    """
    The base class for traits that are components
    """


    # framework data
    category = 'facility'
    # predicate that indicates whether this trait holds a component
    isFacility = True


# end of file
