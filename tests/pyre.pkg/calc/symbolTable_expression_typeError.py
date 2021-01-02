#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Verify that runtime errors in expressions are flagged correctly
    """
    # get the package
    import p2.calc
    # make a simple symbol table so we can build {expressions}
    model = p2.calc.symbolTable()

    # make a couple of variables
    cost = model.variable(name="cost", value=100.)
    shipping = model.variable(name="shipping", value=50.)

    # build an expression with an invalid operation that compiles but fails at runtime
    node = model.expression(value="{cost} & {shipping}")
    # attempt
    try:
        # to evaluate it
        node.getValue()
        # which should fail
        assert False, "unreachable"
    # if it fails by raising the correct exception
    except model.EvaluationError:
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
