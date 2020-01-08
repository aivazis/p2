#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that we can traverse the expression tree correctly and completely
    """

    # access to the basic node
    import p2.algebraic

    # declare a node class
    class node(metaclass=p2.algebraic.algebra, basenode=True): pass

    # declare a couple of nodes
    n1 = node.variable()
    n2 = node.variable()

    # check that they have no dependencies
    assert list(map(id, n1.literals)) == []
    assert list(map(id, n2.literals)) == []
    assert list(map(id, n1.operators)) == []
    assert list(map(id, n2.operators)) == []
    assert list(map(id, n1.variables)) == [id(n1)]
    assert list(map(id, n2.variables)) == [id(n2)]

    # an expression involving a unary operator
    n = -n1
    assert list(map(id, n.operators)) == [id(n)]
    assert list(map(id, n.variables)) == [id(n1)]

    # an expression involving a literal
    n = 2*n1
    assert list(map(id, n.operators)) == [id(n)]
    assert list(map(id, n.variables)) == [id(n1)]

    # an expression involving a binary operator
    n = n1 + n2
    assert list(map(id, n.operators)) == [id(n)]
    assert list(map(id, n.variables)) == [id(n1), id(n2)]

    # add another layer
    m = n + n
    assert list(map(id, m.variables)) == [id(n1), id(n2)] * 2
    assert list(map(id, m.operators)) == [id(m), id(n) ,id(n)]
    # and one more
    l = m + m
    assert list(map(id, l.variables)) == [id(n1), id(n2)] * 4
    assert list(map(id, l.operators)) == [id(l), id(m), id(n), id(n), id(m), id(n), id(n)]

    # a more complicated example
    assert set(map(id, (2*(.5 - n1*n2 + n2**2)*n1).variables)) == {id(n1), id(n2)}

    return


# main
if __name__ == "__main__":
    # do...
    test()


# end of file
