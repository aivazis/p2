# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclasses
from ..descriptors.Public import Public


# declaration
class Trait(Public):
    """
    The base class for component attributes

    Traits extend the notion of the a class attribute to an object that captures metadata that
    has no natural resting place in a regular class declaration.

    Traits enable end-user configurable state, for both simple attributes and references to
    more elaborate objects, such as other components. Collectively, such attributes form the
    component inventory. Inventory items have names that connect them to the configuration
    store, per-instance storage for the attribute value, and additional metadata, such as type
    information, reasonable default values, constraints and validators, documentation, and
    anything else the author of a component deems necessary.
    """


    # framework data
    category = 'trait'   # the stem cell of traits
    origin = None        # the component that declared me into existence
    # structural predicates
    isBehavior = False   # is this public interface?
    isDerivation = False # is the value of this trait derived from the values of other traits?
    isMeasure = False    # does this trait manage a value?
    isProperty = False   # is this a property?
    isFacility = False   # is this a facility?


    # hooks
    def bind(self, client, **kwds):
        """
        Hook invoked when {client}, the class that owns this descriptor, has become aware of it
        """
        # save the client
        self.origin = client
        # all done
        return


# end of file
