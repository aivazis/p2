#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Verify we can compute the pedigree of configurables correctly
    """
    # the configurable base class
    from p2.components.Configurable import Configurable
    # the metaclass
    from p2.components.Requirement import Requirement


    # a class hierarchy
    class Base(Configurable, metaclass=Requirement):
        """
        A direct descendant of configurable
        """

    class Derived(Base):
        """
        An indirect descendant of configurable
        """

    class Other:
        """
        A class that does not inherit from configurable
        """

    class Mixed(Derived, Other):
        """
        A configurable class that also inherits from a non-configurable base
        """

    # verify the pedigree of each class is what we expect
    assert Configurable.pyre_pedigree == ()
    assert Base.pyre_pedigree == (Base,)
    assert Derived.pyre_pedigree == (Derived, Base)
    assert Mixed.pyre_pedigree == (Mixed, Derived, Base)

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
