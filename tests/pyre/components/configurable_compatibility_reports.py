#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


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

    # collect the traits
    base_common = Base.pyre_trait("common")
    derived_common = Derived.pyre_trait("common")
    derived_extra = Derived.pyre_trait("extra")
    ok_common = OK.pyre_trait("common")
    notok_missing = NotOK.pyre_trait("missing")
    badtype_common = BadType.pyre_trait("common")
    shadow_common = Shadow.pyre_trait("common")

    # compatibility checks
    # these ones should succeed
    assert Derived.pyre_isCompatibleWith(Base)
    assert OK.pyre_isCompatibleWith(Base)
    assert Derived.pyre_isCompatibleWith(OK)

    # now the ones that should fail
    report = OK.pyre_isCompatibleWith(Derived, fast=False)
    assert not report
    assert len(report.incompatibilities) == 1
    error = report.incompatibilities[derived_extra][0]
    assert isinstance(error, OK.TraitNotFoundError)

    report = NotOK.pyre_isCompatibleWith(Base, fast=False)
    assert not report
    assert len(report.incompatibilities) == 1
    error = report.incompatibilities[base_common][0]
    assert isinstance(error, NotOK.TraitNotFoundError)

    report = NotOK.pyre_isCompatibleWith(Derived, fast=False)
    assert not report
    assert len(report.incompatibilities) == 2
    error = report.incompatibilities[derived_common][0]
    assert isinstance(error, NotOK.TraitNotFoundError)
    error = report.incompatibilities[derived_extra][0]
    assert isinstance(error, NotOK.TraitNotFoundError)

    report = NotOK.pyre_isCompatibleWith(OK, fast=False)
    assert not report
    assert len(report.incompatibilities) == 1
    error = report.incompatibilities[ok_common][0]
    assert isinstance(error, NotOK.TraitNotFoundError)

    report = BadType.pyre_isCompatibleWith(Base, fast=False)
    assert not report
    assert len(report.incompatibilities) == 1
    error = report.incompatibilities[base_common][0]
    assert isinstance(error, BadType.CategoryMismatchError)

    report = BadType.pyre_isCompatibleWith(Derived, fast=False)
    assert not report
    assert len(report.incompatibilities) == 2
    error = report.incompatibilities[derived_common][0]
    assert isinstance(error, BadType.CategoryMismatchError)
    error = report.incompatibilities[derived_extra][0]
    assert isinstance(error, BadType.TraitNotFoundError)

    report = BadType.pyre_isCompatibleWith(OK, fast=False)
    assert not report
    assert len(report.incompatibilities) == 1
    error = report.incompatibilities[ok_common][0]
    assert isinstance(error, BadType.CategoryMismatchError)

    report = Shadow.pyre_isCompatibleWith(Base, fast=False)
    assert not report
    assert len(report.incompatibilities) == 1
    error = report.incompatibilities[base_common][0]
    assert isinstance(error, Shadow.CategoryMismatchError)

    report = Shadow.pyre_isCompatibleWith(Derived, fast=False)
    assert not report
    assert len(report.incompatibilities) == 2
    error = report.incompatibilities[derived_common][0]
    assert isinstance(error, Shadow.CategoryMismatchError)
    error = report.incompatibilities[derived_extra][0]
    assert isinstance(error, Shadow.TraitNotFoundError)

    report = Shadow.pyre_isCompatibleWith(OK, fast=False)
    assert not report
    assert len(report.incompatibilities) == 1
    error = report.incompatibilities[ok_common][0]
    assert isinstance(error, Shadow.CategoryMismatchError)


    # all done
    return Base, Derived, OK, NotOK, BadType, Shadow


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
