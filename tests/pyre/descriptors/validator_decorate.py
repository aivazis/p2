#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# driver
def test():
    # get the validator class
    from p2.descriptors.Validator import Validator as validator


    # a trait
    class Trait:
        """
        A trait proxy
        """

        def __init__(self, **kwds):
            # chain up
            super().__init__(**kwds)
            # all we care about is a list of validators
            self.validators = []
            # all done
            return


    # a client
    class Component:
        """
        Simple class with a trait
        """

        # declare a trait
        trait = Trait()

        # declare a validator
        @staticmethod
        @validator(descriptors=[trait])
        def squish(value):
            # no op
            return value


    # get the attribute
    trait = Component.trait
    # and the validator
    squish = Component.squish
    # verify the validator has been registered correctly
    assert squish in trait.validators
    # all done
    return trait, squish


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
