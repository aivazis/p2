#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Verify that the portion of the compatibility tests that checks for the presence of traits
    is implemented correctly
    """
    # access the component base class
    from p2.components.Component import Component
    # and the trait classes
    from p2.traits.Measure import Measure as measure
    from p2.traits.Behavior import Behavior as behavior

    # declare a components
    class Base(Component):
        """
        A component
        """
        # with a trait
        common = measure()

    # one that derives from {Base}, so automatically compatible
    class Derived(Base):
        """
        A derived component
        """
        # with an extra trait
        extra = measure()

    # an unrelated component that provides the correct public interface
    class OK(Component):
        """
        Unrelated but compatible
        """
        # because it defines the correct trait
        common = measure()

    # an incompatible one: it's missing the {common} trait
    class NotOK(Component):
        """
        Incompatible
        """
        missing = measure()

    # a component that has a trait by the correct name but it's the wrong type
    class BadType(Component):
        """
        Trait present but of the wrong type
        """
        @behavior
        def common(self):
            """
            behavior, not measure
            """

    # a component that inherits but shadows
    class Shadow(Base):
        """
        Inherit but shadow the trait
        """
        @behavior
        def common(self):
            """
            shadowed by a behavior
            """

    # compatibility checks
    # the ones that should succeed
    assert Derived.pyre_isCompatibleWith(Base)
    assert OK.pyre_isCompatibleWith(Base)
    assert Derived.pyre_isCompatibleWith(OK)
    assert BadType.pyre_isCompatibleWith(Shadow)
    assert Shadow.pyre_isCompatibleWith(BadType)

    # the ones that should fail
    assert not OK.pyre_isCompatibleWith(Derived)
    assert not NotOK.pyre_isCompatibleWith(Base)
    assert not NotOK.pyre_isCompatibleWith(Derived)
    assert not NotOK.pyre_isCompatibleWith(OK)
    assert not BadType.pyre_isCompatibleWith(Base)
    assert not BadType.pyre_isCompatibleWith(Derived)
    assert not BadType.pyre_isCompatibleWith(OK)
    assert not Shadow.pyre_isCompatibleWith(Base)
    assert not Shadow.pyre_isCompatibleWith(Derived)
    assert not Shadow.pyre_isCompatibleWith(OK)

    # all done
    return Base, Derived, OK, NotOK, BadType, Shadow


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
