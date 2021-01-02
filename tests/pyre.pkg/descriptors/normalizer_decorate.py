#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# driver
def test():
    """
    Verify that the {normalizer} can decorate its client methods correctly
    """
    # get the normalizer class
    from p2.descriptors.Normalizer import Normalizer as normalizer


    # a trait
    class Trait:
        """
        A trait proxy
        """

        def __init__(self, **kwds):
            # chain up
            super().__init__(**kwds)
            # all we care about is a list of normalizers
            self.normalizers = []
            # all done
            return


    # a client
    class Component:
        """
        Simple class with a trait
        """

        # declare a trait
        trait = Trait()

        # declare a normalizer
        @staticmethod
        @normalizer(descriptors=[trait])
        def squish(value):
            # no op
            return value


    # get the attribute
    trait = Component.trait
    # and the normalizer
    squish = Component.squish
    # verify the normalizer has been registered correctly
    assert squish in trait.normalizers
    # all done
    return trait, squish


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
