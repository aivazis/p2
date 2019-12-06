# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# superclass
from .Configurable import Configurable
# metaclass
from .Actor import Actor


# declaration
class Component(Configurable, metaclass=Actor):
    """
    The base class for all components
    """


# end of file
