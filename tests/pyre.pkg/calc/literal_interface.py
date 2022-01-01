#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Exercise the interface of literals
    """
    # get the base node from the {calc} package
    from p2.calc.Node import Node as node

    # make a literal
    literal = node.literal(value=0)

    # access the value
    assert literal.getValue() == 0

    # attempt to
    try:
        # set the value
        literal.setValue(value=1)
        # which should fail
        assert False, "unreachable"
    # because {const} is protecting it
    except NotImplementedError as error:
        # all good
        pass

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
