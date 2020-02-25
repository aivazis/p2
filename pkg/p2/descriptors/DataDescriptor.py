# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclass
from .Descriptor import Descriptor


# declaration
class DataDescriptor(Descriptor):
    """
    Mixin class that converts its client into a data descriptor
    """


    # metamethods
    def __set__(self, instance, value):
        """
        Invoked by the interpreter to assign a value to the attribute managed by the descriptor
        """
        # i don't know how to do this; the documentation recommends raising an
        # {AttributeError}, although it doesn't seem to be treated specially
        raise AttributeError(self, instance)


    def __delete__(self, instance):
        """
        Invoked by the interpreter to delete the value of the attribute managed by the descriptor
        """
        # i don't know how to do this
        raise NotImplementedError(f"class '{type(self).__name__}' must implement '__delete__'")


# end of file
