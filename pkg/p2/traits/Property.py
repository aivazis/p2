# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclass
from .Measure import Measure


# declaration
class Property(Measure):
    """
    The base class for traits that are simple types
    """


    # framework data
    category = 'property'
    # predicate that indicates whether this trait is a property
    isProperty = True


# end of file
