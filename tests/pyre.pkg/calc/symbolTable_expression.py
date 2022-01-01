#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Verify expressions resolved against a simple symbol table work as expected
    """
    # access the package
    import p2.calc
    # make a symbol table
    model = p2.calc.symbolTable()

    # make a variable and add it to the model
    cost = model.variable(name="cost", value=100)

    # now an expression
    price = model.expression(name="price", value="2 * {cost}")
    # verify it's an {expression}
    assert isinstance(price, model.node.expression)
    # and that it evaluates correctly
    assert price.getValue() == 2 * cost.getValue()

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
