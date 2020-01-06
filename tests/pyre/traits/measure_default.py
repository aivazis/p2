#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


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
        attr = measure(default=1)


    # get the attribute; careful not to trigger the descriptor behavior
    attr = Component.__dict__["attr"]
    # verify it's a measure
    assert isinstance(attr, measure)
    # verify it has the correct default value
    assert attr.default == 1
    # all done
    return attr


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
