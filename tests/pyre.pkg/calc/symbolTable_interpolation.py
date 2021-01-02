#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Verify interpolations resolved against a simple symbol table work as expected
    """
    # access the package
    import p2.calc
    # make a symbol table
    model = p2.calc.symbolTable()

    # make a variable
    home = model.variable(value="/home/pyre")
    # add it to the model
    model.insert(name="home", node=home)

    # now an expression
    tools = model.interpolation(value="{home}/tools")
    # verify it's an {expression}
    assert isinstance(tools, model.node.interpolation)
    # and that it evaluates correctly
    assert tools.getValue() == "/home/pyre/tools"

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
