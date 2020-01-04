#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


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


    # set the {Base} measure
    Base.bm = 2
    # verify that this assignment did not disturb the descriptor
    assert isinstance(Base.__dict__["bm"], measure)
    # access the {Base} measure
    assert Base.bm == 2
    # verify {Derived} inherits the new default
    assert Derived.bm == 2

    # set the {Derived} measures
    Derived.dm = False
    Derived.bm = 3
    # verify that this assignment did not disturb the descriptor
    assert isinstance(Derived.__dict__["dm"], measure)
    # access the {Derived} measures
    assert Derived.dm == False
    assert Derived.bm == 3
    # verify {Shadow} inherits correctly
    assert Shadow.dm == False

    # set the {Shadow} measure
    Shadow.bm = "another value"
    Shadow.dm = None
    # verify that this assignment did not disturb the descriptor
    assert isinstance(Shadow.__dict__["bm"], measure)
    # access the {Shadow} measures
    assert Shadow.bm == "another value"
    assert Shadow.dm == None
    # verify its base classes are unaffected
    assert Base.bm == 2
    assert Derived.bm == 3
    assert Derived.dm == False

    # all done
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
