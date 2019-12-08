# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# superclass
from .Configurable import Configurable


# declaration
class Property(Configurable):
    """
    The base class for traits that are simple types
    """


    # framework data
    category = 'property'
    # predicate that indicates whether this trait is a property
    isProperty = True


# end of file
