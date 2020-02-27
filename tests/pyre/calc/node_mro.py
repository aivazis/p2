#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Sanity test: make sure the module is accessible
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
    assert nodeMRO == [ node, algebra.base, calculator.arithmetic, object ]

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
