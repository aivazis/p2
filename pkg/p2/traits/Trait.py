# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# superclasses
from ..descriptors.Public import Public
from ..descriptors.Descriptor import Descriptor


# declaration
class Trait(Descriptor, Public):
    """
    The base class for component attributes

    Traits extend the notion of the a class attribute to an object that captures meta-data that
    has no natural resting place in a regular class declaration.

    Traits enable end-user configurable state, for both simple attributes and reference to more
    elaborate object, such as other components. Collectively, such attributes from the
    component inventory. Inventory items have names that connect them to the configuration
    store, per-instance storage for the attribute value, and additional meta-data, such as type
    information, reasonable default values, constraints and validators, documentation, and
    anything else the author of a component deems necessary.
    """


    # framework data
    category = 'trait' # the stem cell of traits
    # predicate that indicates whether this trait is a behavior
    isBehavior = False
    # predicate that indicates whether this trait is subject to runtime configuration
    isConfigurable = False
    # predicate that indicates whether this trait is a property
    isProperty = False
    # predicate that indicates whether this trait is a facility
    isFacility = False




# end of file
