#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# get the property class
from p2.traits.Property import Property as property


# a client
class Component:
    """
    Simple class with a property
    """

    # declare a property
    attr = property()


# driver
def test():
    # get the attribute; careful not to trigger the descriptor behavior
    attr = Component.__dict__["attr"]
    # verify it's a property
    assert isinstance(attr, property)
    # verify it has the right category name
    assert attr.category == "property"
    # and that the trait predicates have the right values
    assert attr.isBehavior == False
    assert attr.isConfigurable == True
    assert attr.isProperty == True
    assert attr.isFacility == False
    # all done
    return attr


# bootstrap
if __name__ == "__main__":
    # run the test
    test()


# end of file