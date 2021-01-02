#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Verify that expressions that contain syntax errors are flagged correctly
    """
    # get the package
    import p2.calc
    # make a simple symbol table so we can build {expressions}
    model = p2.calc.symbolTable()

    # try one
    try:
        # with an unbalanced parenthesis
        model.expression(value="2 * ({cost} + {shipping}")
        # it should fail
        assert False, "unreachable"
    # if it fails as expected
    except model.ExpressionSyntaxError:
        # all good
        pass

    # try one
    try:
        # with a missing operand
        model.expression(value="2 * ({cost} + )")
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
