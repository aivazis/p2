# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# parasim
# (c) 1998-2019 all rights reserved
#


# publish
from . import meta


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


# end of file
