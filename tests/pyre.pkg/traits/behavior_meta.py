#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# driver
def test():
    """
    Verify that the behavior decorator works as expected when invoked with metadata
    """

    # get the behavior class
    from p2.traits.Behavior import Behavior as behavior


    # a client
    class Component:
        """
        Simple class with a behavior
        """

        # declare a behavior
        @behavior(tip="a simple method")
        def method(self):
            """
            A simple method
            """
            return True


    # get the attribute; careful not to trigger the descriptor behavior
    method = Component.__dict__["method"]
    # verify it's a behavior
    assert isinstance(method, behavior)
    # verify it has the right name
    assert method.name == "method"
    # and that it got decorated correctly
    assert method.tip == "a simple method"
    assert method.doc.strip() == "A simple method"
    # all done
    return method


# bootstrap
if __name__ == "__main__":
    # run the test
    test()


# end of file
