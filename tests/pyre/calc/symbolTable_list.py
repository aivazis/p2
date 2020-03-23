#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Exercise creating and inserting a list into a simple symbol table
    """
    # access the package
    import p2.calc
    # make a symbol table
    model = p2.calc.symbolTable()

    # make a list of numbers
    values = (95, 100, 90, 95, 100, 90, 85)
    # add it to the model as a node
    grades = model.list(name="grades", value=values)

    # check the keys
    assert set(model.keys()) == {"grades"}
    # check the nodes
    assert set(model.nodes()) == {grades}
    # check the value
    assert grades.getValue() == list(values)

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
