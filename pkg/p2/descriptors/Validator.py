# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclass
from .Processor import Processor


# declaration
class Validator(Processor):
    """
    A method decorator that registers its client as a validator of descriptor values
    """


    # meta-methods
    def __call__(self, method):
        """
        Add {method} as a validator to my registered descriptors
        """
        # go through the sequence of registered descriptors
        for descriptor in self.descriptors:
            # and register {method} as a validator
            descriptor.validators.append(method)
        # all done
        return method


# end of file
