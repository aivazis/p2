# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# superclass
from .Trait import Trait


# declaration
class Configurable(Trait):
    """
    The base class of all traits that require storage for user configurable state
    """


    # framework data
    category = 'configurable'
    # predicate that indicates whether this trait is subject to runtime configuration
    isConfigurable = True


# end of file