#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# driver
def test():
    """
    Verify that measures get the correct category predicates
    """

    # get the measure trait class
    from p2.traits.Measure import Measure as measure


    # a client
    class Component:
        """
        Simple class with a measure
        """

        # declare a measure
        attr = measure()


    # get the attribute; careful not to trigger the descriptor behavior
    attr = Component.__dict__["attr"]
    # verify it's a measure
    assert isinstance(attr, measure)
    # verify it has the right category name
    assert attr.category == "measure"
    # and that the trait predicates have the right values
    assert attr.isBehavior == False
    assert attr.isDerivation == False
    assert attr.isMeasure == True
    assert attr.isProperty == False
    assert attr.isFacility == False
    # all done
    return attr


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
