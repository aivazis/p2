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


# end of file
