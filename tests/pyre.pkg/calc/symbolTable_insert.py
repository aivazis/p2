#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Exercise inserting a couple of nodes into a simple symbol table
    """
    # access the package
    import p2.calc
    # make a symbol table
    model = p2.calc.symbolTable()

    # make a couple of variables
    cost = model.variable(value=100)
    price = 2 * cost

    # add them to the model
    model.insert(name="cost", node=cost)
    model.insert(name="price", node=price)

    # check the keys
    assert set(model.keys()) == {"cost", "price"}
    # check the nodes
    assert set(model.nodes()) == {cost, price}

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
