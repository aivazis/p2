#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# driver
def test():
    """
    Verify that behaviors get the correct category predicates
    """

    # get the behavior class
    from p2.traits.Behavior import Behavior as behavior


    # a client
    class Component:
        """
        Simple class with a behavior
        """

        # declare a behavior
        @behavior
        def method(self):
            """
            A simple method
            """
            return True


    # get the attribute; careful not to trigger the descriptor behavior
    attr = Component.__dict__["method"]
    # verify it's a behavior
    assert isinstance(attr, behavior)
    # verify it has the right category name
    assert attr.category == "behavior"
    # and that the trait predicates have the right values
    assert attr.isBehavior == True
    assert attr.isMeasure == False
    assert attr.isDerivation == False
    assert attr.isProperty == False
    assert attr.isFacility == False
    # all done
    return attr


# bootstrap
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
