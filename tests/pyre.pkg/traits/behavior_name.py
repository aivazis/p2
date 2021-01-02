#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# driver
def test():
    """
    Verify that behaviors register their name correctly
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
    # verify it has the right name
    assert attr.name == "method"
    # all done
    return attr


# bootstrap
if __name__ == "__main__":
    # run the test
    test()


# end of file
