#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


def test():
    """
    Verify that component measures are harvested correctly
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


    # the list of trait names for {Base}
    localNames = ["bm"]
    # check the traits
    assert Base.pyre_localTraits == tuple(map(Base.pyre_trait, localNames))
    assert Base.pyre_inheritedTraits == ()
    assert tuple(Base.pyre_traits()) == Base.pyre_localTraits + Base.pyre_inheritedTraits

    # the list of trait name for {Derived}
    localNames =  ["dm"]
    inheritedNames =  ["bm"]
    # check the traits
    assert Derived.pyre_localTraits == tuple(map(Derived.pyre_trait, localNames))
    assert Derived.pyre_inheritedTraits == tuple(map(Derived.pyre_trait, inheritedNames))
    assert tuple(Derived.pyre_traits()) == Derived.pyre_localTraits + Derived.pyre_inheritedTraits

    # the list of trait name for {Shadow}
    localNames =  ["bm"]
    inheritedNames =  ["dm"]
    # check the traits
    assert Shadow.pyre_localTraits == tuple(map(Shadow.pyre_trait, localNames))
    assert Shadow.pyre_inheritedTraits == tuple(map(Shadow.pyre_trait, inheritedNames))
    assert tuple(Shadow.pyre_traits()) == Shadow.pyre_localTraits + Shadow.pyre_inheritedTraits

    # all done
    return




# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
