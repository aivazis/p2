#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that we can successfully perform surgery in an expression tree
    """

    # access to the package
    import p2.algebraic

    # declare a node class
    class node(metaclass=p2.algebraic.algebra, basenode=True):
        """
        The base node
        """

        class literal:
            """
            An implementation of literals
            """
            # public data
            value = None
            # metamethods
            def __init__(self, value, **kwds):
                # chain up
                super().__init__(**kwds)
                # save the value
                self.value = value
                # all done
                return


    # declare a couple of nodes
    n1 = node.variable()
    n2 = node.variable()
    n3 = node.variable()

    # careful with comparisons: do not trigger operator _eq_!
    # check that they have no dependencies
    assert list(map(id, n1.variables)) == [id(n1)]
    assert list(map(id, n2.variables)) == [id(n2)]
    assert list(map(id, n3.variables)) == [id(n3)]

    # a simple expression
    n = n1 + n2
    assert list(map(id, n.variables)) == [id(n1), id(n2)]
    # patch {n3} in
    n.substitute(current=n1, replacement=n3)
    # and check that it happened correctly
    assert list(map(id, n.variables)) == [id(n3), id(n2)]

    # add another layer
    m = n1 + n2 + n3
    assert list(map(id, m.variables)) == [id(n1), id(n2), id(n3)]
    # patch {n} in
    m.substitute(current=n3, replacement=n)
    # check
    assert list(map(id, m.variables)) == [id(n1), id(n2), id(n3), id(n2)]

    # a more complicated example
    n = (2*(n1**2 - 2*n1*n2 + n2**2)*n3)
    assert set(map(id, n.variables)) == {id(n1), id(n2), id(n3)}
    # patch {n3} in
    n.substitute(current=n1, replacement=n3)
    # and check that it happened correctly
    assert set(map(id, n.variables)) == {id(n2), id(n3)}

    # let's try
    try:
        # to make a cycle
        n.substitute(current=n2, replacement=n)
        # which should fail
        assert False, "unreachable"
    # catch it
    except n.CircularReferenceError:
        # all good
        pass

    # all done
    return


# main
if __name__ == "__main__":
    # do...
    test()


# end of file
