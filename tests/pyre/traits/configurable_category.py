#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# get the configurable trait class
from p2.traits.Configurable import Configurable as configurable


# a client
class Component:
    """
    Simple class with a configurable trait
    """

    # declare a configurable trait
    attr = configurable()


# driver
def test():
    # get the attribute; careful not to trigger the descriptor behavior
    attr = Component.__dict__["attr"]
    # verify it's a configurable trait
    assert isinstance(attr, configurable)
    # verify it has the right category name
    assert attr.category == "configurable"
    # and that the trait predicates have the right values
    assert attr.isBehavior == False
    assert attr.isConfigurable == True
    assert attr.isProperty == False
    assert attr.isFacility == False
    # all done
    return attr


# bootstrap
if __name__ == "__main__":
    # run the test
    test()


# end of file
