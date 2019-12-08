# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# declaration
class Descriptor:
    """
    Mixin class that converts its client into a descriptor
    """


    # framework hook
    def bind(self, **kwds):
        """
        Notification that the {component} class that owns this trait has become aware of it
        """
        # by default, there's nothing to do; subclasses may override and chain up to here
        return self


    # meta-methods
    def __get__(self, instance, cls):
        """
        Invoked by the interpreter to retrieve the value of a trait
        """


    def __set__(self, instance, value):
        """
        Invoked by the interpreter to assign a value to a trait
        """


# end of file
