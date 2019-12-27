# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# superclass
from .Configurable import Configurable
# metaclass
from .Actor import Actor
# the base protocol
from .Protocol import Protocol


# declaration
class Component(Configurable, metaclass=Actor):
    """
    The base class for all components
    """


    # framework data
    # structural
    pyre_inventory = None    # trait value management
    pyre_protocol = Protocol # my default protocol; overwritten by {Actor} during construction
    # type id
    pyre_isComponent = True


    # metamethods
    def __init__(self, name=None, **kwds):
        # chain up
        super().__init__(**kwds)
        # save my name
        self.pyre_name = name
        # all done
        return


    def __str__(self):
        """
        Build a human readable representation
        """
        # accumulator of the name fragments
        fragments = []

        # get my name
        name = self.pyre_name
        # if i have one
        if name is not None:
            # use it
            fragments.append(f"component '{name}'")
        # otherwise
        else:
            # mark the component a s private
            fragments.append("unnamed component")

        # get my family name
        family = self.pyre_family
        # if i have one
        if family is not None:
            # use it
            fragments.append(f"an instance of '{family}'")
        # otherwise
        else:
            # get my class name and use it
            fragments.append(f"an instance of '{type(self).__name__}'")

        # assemble and return
        return ", ".join(fragments)


# end of file
