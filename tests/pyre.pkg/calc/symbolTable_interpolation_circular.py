#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Verify that interpolations that contain circular references are flagged correctly
    """
    # get the package
    import p2.calc
    # make a simple symbol table so we can build {interpolations}
    model = p2.calc.symbolTable()

    # verify it's empty
    assert tuple(model.keys()) == ()

    # try one
    try:
        # with an immediate circular reference
        model.interpolation(name="home", value="{home}")
        # it should fail
        assert False, "unreachable"
    # if it fails as expected
    except model.CircularReferenceError:
        # all good
        pass

    # we should have only one node in the table
    assert set(model.keys()) == {"home"}
    # and the corresponding node should be {unresolved}
    assert isinstance(model.resolve(name="home"), model.node.unresolved)

    # set up a cycle: {tools} is equal to {home}
    model.interpolation(name="tools", value="{home}")
    # and now, try to
    try:
        # set {home} equal to {tools}
        model.interpolation(name="home", value="{tools}")
        # which should fail
        assert False, "unreachable"
    # if it fails as expected
    except model.CircularReferenceError:
        # all good
        pass

    # all done
    return


# main
if __name__ == "__main__":
    # request debugging support for the {p2.calc} package
    pyre_debug = { "p2.calc" }
    # run the test
    test()
    # verify reference counts
    from p2.calc.Node import Node as node
    # verify all nodes have been destroyed
    assert len(node.pyre_extent) == 0


# end of file
