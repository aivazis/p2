#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# get the facility class
from p2.traits.Facility import Facility as facility


# a client
class Component:
    """
    Simple class with a facility
    """

    # declare a facility
    attr = facility()


# driver
def test():
    # get the attribute; careful not to trigger the descriptor behavior
    attr = Component.__dict__["attr"]
    # verify it's a facility
    assert isinstance(attr, facility)
    # verify it has the right category name
    assert attr.category == "facility"
    # and that the trait predicates have the right values
    assert attr.isBehavior == False
    assert attr.isConfigurable == True
    assert attr.isProperty == False
    assert attr.isFacility == True
    # all done
    return attr


# bootstrap
if __name__ == "__main__":
    # run the test
    test()


# end of file
