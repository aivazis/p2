#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# driver
def test():
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
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
