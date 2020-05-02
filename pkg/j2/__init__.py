# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# administrative
def copyright():
    """
    Return the journal copyright note
    """
    return print(meta.header)


def license():
    """
    Print the journal license
    """
    # print it
    return print(meta.license)


def version():
    """
    Return the journal version
    """
    return meta.version


def credits():
    """
    Print the acknowledgments
    """
    # print it
    return print(meta.acknowledgments)


# publish
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
if not without_libjournal:
    # load the bindings
    from .ext import libjournal
    # if something went wrong
    if libjournal is None:
        # indicate that we don't have access to the bindings
        without_libjournal = True

# publish the package metadata
from . import meta

# if we don't have access to the bindings
if without_libjournal:
    # publish the keeper of the global settings
    from .Chronicler import Chronicler
    # instantiate the singleton and publish the instance
    chronicler = Chronicler()

    # devices
    from .Trash import Trash as trash
    from .Console import Console as cout
    from .ErrorConsole import ErrorConsole as cerr

    # channels
    # developer facing
    from .Debug import Debug as debug
    from .Firewall import Firewall as firewall
    # user facing
    from .Informational import Informational as info
    from .Warning import Warning as warning
    from .Error import Error as error

# if we have access to the bindings
else:
    # let the c++ library take over
    # publish the keeper of the global state
    chronicler = libjournal.Chronicler

    # devices
    trash = libjournal.Trash
    cout = libjournal.Console
    cerr = libjournal.ErrorConsole

    # the developer facing channels
    debug = libjournal.Debug
    firewall = libjournal.Firewall
    # the user facing channels
    info = libjournal.Informational
    warning = libjournal.Warning
    error = libjournal.Error


# end of file
