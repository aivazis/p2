#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Verify that interpolations that contain unbalanced braces are flagged correctly
    """
    # get the package
    import p2.calc
    # make a simple symbol table so we can build {interpolations}
    model = p2.calc.symbolTable()

    # try one
    try:
        # with a single unbalanced opening brace
        model.interpolation(value="{")
        # it should fail
        assert False, "unreachable"
    # if it fails as expected
    except model.ExpressionSyntaxError:
        # all good
        pass

    # try one
    try:
        # with a single unbalanced closing brace
        model.interpolation(value="}")
        # it should fail
        assert False, "unreachable"
    # if it fails as expected
    except model.ExpressionSyntaxError:
        # all good
        pass

    # try one
    try:
        # with an unbalanced opening brace
        model.interpolation(value="{{home}/tools")
        # it should fail
        assert False, "unreachable"
    # if it fails as expected
    except model.ExpressionSyntaxError:
        # all good
        pass

    # try one
    try:
        # with an unbalanced closing brace
        model.interpolation(value="/home/{tools}}")
        # it should fail
        assert False, "unreachable"
    # if it fails as expected
    except model.ExpressionSyntaxError:
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
