#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Verify that component measures are harvested correctly
    """
    # the component superclass
    from p2.components.Component import Component
    # the trait factory
    from p2.traits.Behavior import Behavior as behavior


    # subclass
    class Base(Component):
        """
        A simple component
        """

        @behavior(tip='a simple behavior')
        def bb(self):
            return 1


    class Derived(Base):
        """
        A derived component
        """

        @behavior(tip='another simple behavior')
        def db(self):
            return True


    class Shadow(Derived):
        """
        A component that redeclares ancestor traits
        """

        @behavior(tip='a shadowing behavior')
        def bb(self):
            return "a string"


    # the list of trait names for {Base}
    localNames = ["bb"]
    # check the traits
    assert Base.pyre_localTraits == tuple(map(Base.pyre_trait, localNames))
    assert Base.pyre_inheritedTraits == ()
    assert tuple(Base.pyre_traits()) == Base.pyre_localTraits + Base.pyre_inheritedTraits

    # the list of trait name for {Derived}
    localNames =  ["db"]
    inheritedNames =  ["bb"]
    # check the traits
    assert Derived.pyre_localTraits == tuple(map(Derived.pyre_trait, localNames))
    assert Derived.pyre_inheritedTraits == tuple(map(Derived.pyre_trait, inheritedNames))
    assert tuple(Derived.pyre_traits()) == Derived.pyre_localTraits + Derived.pyre_inheritedTraits

    # the list of trait name for {Shadow}
    localNames =  ["bb"]
    inheritedNames =  ["db"]
    # check the traits
    assert Shadow.pyre_localTraits == tuple(map(Shadow.pyre_trait, localNames))
    assert Shadow.pyre_inheritedTraits == tuple(map(Shadow.pyre_trait, inheritedNames))
    assert tuple(Shadow.pyre_traits()) == Shadow.pyre_localTraits + Shadow.pyre_inheritedTraits

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
