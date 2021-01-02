#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


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

        # a simple measure
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


    # instantiate
    base = Base()
    # the list of trait names for {Base}
    localNames = ["bm"]
    # check the traits
    assert base.pyre_localTraits == tuple(map(base.pyre_trait, localNames))
    assert base.pyre_inheritedTraits == ()
    assert tuple(base.pyre_traits()) == base.pyre_localTraits + base.pyre_inheritedTraits

    # instantiate {derived}
    derived = Derived()
    # the list of trait name for {Derived}
    localNames =  ["dm"]
    inheritedNames =  ["bm"]
    # check the traits
    assert derived.pyre_localTraits == tuple(map(derived.pyre_trait, localNames))
    assert derived.pyre_inheritedTraits == tuple(map(derived.pyre_trait, inheritedNames))
    assert tuple(derived.pyre_traits()) == derived.pyre_localTraits + derived.pyre_inheritedTraits

    # instantiate {Shadow}
    shadow = Shadow()
    # the list of trait name for {Shadow}
    localNames =  ["bm"]
    inheritedNames =  ["dm"]
    # check the traits
    assert shadow.pyre_localTraits == tuple(map(shadow.pyre_trait, localNames))
    assert shadow.pyre_inheritedTraits == tuple(map(shadow.pyre_trait, inheritedNames))
    assert tuple(shadow.pyre_traits()) == shadow.pyre_localTraits + shadow.pyre_inheritedTraits

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
