#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Verify that the {node} class hierarchy looks as expected
    """
    # get the {calc}
    import p2.calc
    # and {algebraic} packages
    import p2.algebraic

    # access
    from p2.calc.Node import Node as node

    # pull out the {calc} metaclass
    calculator = p2.calc.calculator
    # and the base metaclass
    algebra = p2.algebraic.algebra

    # get the base node {mro}
    nodeMRO = node.mro()
    # verify the derivation of the base node
    assert nodeMRO == [ node, calculator.base, algebra.base, calculator.arithmetic, object ]

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
