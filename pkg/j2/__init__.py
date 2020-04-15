# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# administrative
def copyright():
    """
    Return the pyre copyright note
    """
    return print(meta.header)


def license():
    """
    Print the pyre license
    """
    # print it
    return print(meta.license)


def version():
    """
    Return the pyre version
    """
    return meta.version


def credits():
    """
    Print the acknowledgments
    """
    # print it
    return print(meta.acknowledgments)


# publish
# the metadata
from . import meta
# the bindings
from .ext import libjournal


# if there is no functional extension module
if True:
    # publish
    # the devices
    from .Trash import Trash as trash
    from .Console import Console as cout
    from .ErrorConsole import ErrorConsole as cerr

    # the channels
    from .Debug import Debug as debug
    from .Informational import Informational as info

    # get the singleton with the global state
    from .Chronicler import Chronicler as chronicler
    # attach the default device
    chronicler().device = cout()


# end of file
