#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# get the trait class
from p2.traits.Trait import Trait as trait


# a client
class Component:
    """
    Simple class with a trait
    """

    # declare a traits
    attr = trait()


# driver
def test():
    # get the attribute; careful not to trigger the descriptor behavior
    attr = Component.__dict__["attr"]
    # verify it's a trait
    assert isinstance(attr, trait)
    # verify it has the right name
    assert attr.name == "attr"
    # verify that the aliases are initialized properly
    assert attr.aliases == { "attr" }
    # all done
    return 0


# bootstrap
if __name__ == "__main__":
    # run the test
    status = test()
    # share the status code with the shell
    raise SystemExit(status)


# end of file
