# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# declaration
class Descriptor:
    """
    Mixin class that converts its client into a non-data descriptor
    """


    # meta-methods
    def __get__(self, instance, cls):
        """
        Invoked by the interpreter to retrieve the value of a descriptor
        """
        # i don't know how to do this
        raise NotImplementedError(f"class '{type(self).__name__}' must implement '__get__'")


# end of file
