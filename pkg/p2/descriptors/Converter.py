# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# superclass
from .Processor import Processor


# declaration
class Converter(Processor):
    """
    A method decorator that registers its client as a converter of descriptor values
    """


    # metamethods
    def __call__(self, method):
        """
        Add {method} as a converter to my registered descriptors
        """
        # go through the sequence of registered descriptors
        for descriptor in self.descriptors:
            # and register {method} as a converter
            descriptor.converters.append(method)
        # all done
        return method


# end of file
