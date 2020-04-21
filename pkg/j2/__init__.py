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

# set up a marker about whether we are going to load and publish the bindings
without_libjournal = False

# get the {__main__} module
import __main__
# check whether
try:
    # the user has expressed an opinion
    without_libjournal = __main__.journal_no_libjournal
# if not
except AttributeError:
    # no worries
    pass

# if we are allowed
if without_libjournal is False:
    # load the bindings
    from .ext import libjournal
    # if something went wrong
    if libjournal is None:
        # indicate that we don't have access to the binding
        without_libjournal = True

# if there is no functional extension module
if without_libjournal:
    # fall back on the pure python implementation
    # the devices
    from .Trash import Trash as trash
    from .Stream import Stream as stream
    from .Console import Console as cout
    from .ErrorConsole import ErrorConsole as cerr

    # the channels
    from .Null import Null as null

    from .Debug import Debug as debug
    from .Firewall import Firewall as firewall

    from .Informational import Informational as info
    from .Warning import Warning as warning
    from .Error import Error as error

    # get the singleton with the global state
    from .Chronicler import Chronicler as chronicler
    # attach the default device
    chronicler().device = cout()

# otherwise
else:
    # minimal configuration, for now
    # get the console
    from .Console import Console as cout
    # get the singleton with the global state
    from .Chronicler import Chronicler as chronicler
    # attach the default device
    chronicler().device = cout()


# end of file
