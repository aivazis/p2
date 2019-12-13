# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# superclass
from .Trait import Trait


# declaration
class Measure(Trait):
    """
    The base class of all traits that require storage for user configurable state
    """


    # framework data
    category = 'measure'
    # predicate that indicates whether this trait is subject to runtime configuration
    isMeasure = True


# end of file
