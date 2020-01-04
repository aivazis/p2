#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# driver
def test():
    """
    Verify that facilities get the correct category predicates
    """

    # get the facility class
    from p2.traits.Facility import Facility as facility


    # a client
    class Component:
        """
        Simple class with a facility
        """

        # declare a facility
        attr = facility()


    # get the attribute; careful not to trigger the descriptor behavior
    attr = Component.__dict__["attr"]
    # verify it's a facility
    assert isinstance(attr, facility)
    # verify it has the right category name
    assert attr.category == "facility"
    # and that the trait predicates have the right values
    assert attr.isBehavior == False
    assert attr.isMeasure == True
    assert attr.isDerivation == False
    assert attr.isProperty == False
    assert attr.isFacility == True
    # all done
    return attr


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
