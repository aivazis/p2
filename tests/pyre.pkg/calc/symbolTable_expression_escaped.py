#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Verify that the escaping mechanism works as expected
    """
    # get the package
    import p2.calc
    # make a simple symbol table so we can build {expressions}
    model = p2.calc.symbolTable()

    # attempt to build an expression with no references
    node = model.expression(value="2 * ({{cost}} + {{shipping}})")
    # the return {node} should be a {variable} since there is no expression to evaluate
    assert isinstance(node, model.node.variable)
    # and its value should be as above but with the double braces replaced with single ones
    assert node.getValue() == "2 * ({cost} + {shipping})"

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
