#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Verify that the simple symbol table can be instantiated from the package level factory
    """
    # access the package
    import p2.calc
    # make a symbol table
    p2.calc.symbolTable()
    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
