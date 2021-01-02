# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# superclass
from .Processor import Processor


# declaration
class Normalizer(Processor):
    """
    A method decorator that registers its client as a normalizer of descriptor values
    """


    # metamethods
    def __call__(self, method):
        """
        Add {method} as a normalizer to my registered descriptors
        """
        # go through the sequence of registered descriptors
        for descriptor in self.descriptors:
            # and register {method} as a normalizer
            descriptor.normalizers.append(method)
        # all done
        return method


# end of file
