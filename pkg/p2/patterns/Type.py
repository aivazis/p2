# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# declaration
class Type(type):
    """
    The base meta-class from which all pyre meta-classes derive

    The main raison d'être for this class is to absorb any {**kwds} arguments passed to
    {__new__} and {__init__} before chaining up to their implementations in {type}.
    """


    # meta methods
    def __new__(cls, name, bases, attributes, **kwds):
        """
        Create a new class record
        """
        # swallow the keyword arguments and chain up
        return super().__new__(cls, name, bases, attributes)


    def __init__(self, name, bases, attributes, **kwds):
        """
        Initialize a class record
        """
        # swallow the keyword arguments and chain up
        return super().__init__(name, bases, attributes)


# end of file
