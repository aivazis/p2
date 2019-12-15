#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


def test():
    """
    Verify that attribute values can be retrieve correctly
    """
    # the component superclass
    from p2.components.Component import Component
    # the trait factory
    from p2.traits.Measure import Measure as measure


    # subclass
    class Base(Component):
        """
        A simple component
        """

        bm = measure()
        bm.default = 1
        bm.tip = 'a simple value'


    class Derived(Base):
        """
        A derived component
        """

        # a simple measure
        dm = measure()
        dm.default = True
        dm.tip = 'another simple value'


    class Shadow(Derived):
        """
        A component that redeclares ancestor traits
        """

        bm = measure()
        bm.default = "a value"
        bm.tip = 'a shadowing value'


    # access the {Base} measure
    assert Base.bm == 1
    # access the {Derived} measures
    assert Derived.dm == True
    assert Derived.bm == 1
    # access the {Shadow} measures
    assert Shadow.bm == "a value"
    assert Shadow.dm == True

    # all done
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
