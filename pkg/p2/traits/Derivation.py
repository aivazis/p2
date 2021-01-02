# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# superclasses
from .Trait import Trait
from ..descriptors.Descriptor import Descriptor


# declaration
class Derivation(Trait, Descriptor):
    """
    The base class of all traits whose values are derived from expressions
    """


    # framework data
    category = 'derivation'
    # predicate that indicates whether this trait is a derivation
    isDerivation = True


# end of file
