# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# declaration
class Descriptor:
    """
    Mixin class that converts its client into a non-data descriptor
    """


    # framework hook
    def bind(self, **kwds):
        """
        Notification that the class that owns this descriptor has become aware of it
        """
        # by default, there's nothing to do; subclasses may override and chain up to here
        return self


    # meta-methods
    def __get__(self, instance, cls):
        """
        Invoked by the interpreter to retrieve the value of a descriptor
        """
        # i don't know how to do this
        raise NotImplementedError(f"class '{type(self).__name__}' must implement '__get__'")


# end of file
