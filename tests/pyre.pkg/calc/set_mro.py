#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Verify that the {set} class hierarchy looks as expected
    """
    # get the {calc}
    from p2.calc import calculator
    # and {algebraic} metaclasses
    from p2.algebraic import algebra

    # get the base node from the {calc} package
    from p2.calc.Node import Node as node

    # get the base node {mro}
    nodeMRO = node.mro()

    # get the set class
    set = node.set
    # and its mro
    setMRO = set.mro()
    # verify the structure
    assert setMRO == [
        # the user visible class
        set,
        # observer
        calculator.dependent, calculator.observer,
        # observable
        calculator.dependency, calculator.observable, calculator.reactor,
        # base {set} from {calculator}
        calculator.set,
        # base {sequence} from {calculator}
        calculator.sequence,
        # composite
        node.composite, algebra.composite
        # node
        ] + nodeMRO

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
