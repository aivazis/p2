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


    # instantiate
    base = Base()
    # the list of trait names for {base}
    localNames = ["bb"]
    # check the traits
    assert base.pyre_localTraits == tuple(map(base.pyre_trait, localNames))
    assert base.pyre_inheritedTraits == ()
    assert tuple(base.pyre_traits()) == base.pyre_localTraits + base.pyre_inheritedTraits

    # instantiate
    derived = Derived()
    # the list of trait name for {derived}
    localNames =  ["db"]
    inheritedNames =  ["bb"]
    # check the traits
    assert derived.pyre_localTraits == tuple(map(derived.pyre_trait, localNames))
    assert derived.pyre_inheritedTraits == tuple(map(derived.pyre_trait, inheritedNames))
    assert tuple(derived.pyre_traits()) == derived.pyre_localTraits + derived.pyre_inheritedTraits

    # instantiate
    shadow = Shadow()
    # the list of trait name for {shadow}
    localNames =  ["bb"]
    inheritedNames =  ["db"]
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
