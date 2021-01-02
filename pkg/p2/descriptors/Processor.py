# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# declaration
class Processor:
    """
    The base class for decorators that attach value processors to descriptors
    """


    # public data
    descriptors = () # the sequence of descriptors that i decorate


    # metamethods
    def __init__(self, descriptors=descriptors, **kwds):
        # chain up
        super().__init__(**kwds)
        # record which descriptors i decorate
        self.descriptors = tuple(descriptors)
        # all done
        return


    def __call__(self, method):
        # don't know how to do that
        raise NotImplementedError(f"class '{type(self).__name__}' must implement '__call__'")


# end of file
