# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# superclass
from .Trait import Trait


# declaration
class Derivation(Trait):
    """
    The base class of all traits whose values are derived from expressions
    """


    # framework data
    category = 'derivation'
    # predicate that indicates whether this trait is a derivation
    isDerivation = True


# end of file
