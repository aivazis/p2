#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# driver
def test():
    """
    Verify that properties get the correct category predicates
    """

    # get the property class
    from p2.traits.Property import Property as property


    # a client
    class Component:
        """
        Simple class with a property
        """

        # declare a property
        attr = property()


    # get the attribute; careful not to trigger the descriptor behavior
    attr = Component.__dict__["attr"]
    # verify it's a property
    assert isinstance(attr, property)
    # verify it has the right category name
    assert attr.category == "property"
    # and that the trait predicates have the right values
    assert attr.isBehavior == False
    assert attr.isDerivation == False
    assert attr.isMeasure == True
    assert attr.isProperty == True
    assert attr.isFacility == False
    # all done
    return attr


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
