# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# superclass
from .Configurable import Configurable
# metaclass
from .Role import Role


# declaration
class Protocol(Configurable, metaclass=Role, internal=True):
    """
    The base class for requirement specifications
    """


# end of file
