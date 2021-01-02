#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Verify that the {variable} class hierarchy looks as expected
    """
    # get the {calc}
    from p2.calc import calculator
    # and {algebraic} metaclasses
    from p2.algebraic import algebra

    # get the base node from the {calc} package
    from p2.calc.Node import Node as node

    # get the base node {mro}
    nodeMRO = node.mro()

    # get the variable class
    variable = node.variable
    # and its mro
    variableMRO = variable.mro()
    # verify the structure
    assert variableMRO == [
        # the user visible class
        variable,
        # observable
        calculator.dependency, calculator.observable, calculator.reactor,
        # value management
        calculator.value,
        # base {variable} from {algebra}
        algebra.variable, algebra.leaf
        # node
        ] + nodeMRO

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
