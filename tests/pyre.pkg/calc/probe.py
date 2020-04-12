#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


#
def test():
    """
    Verify that probes get notified when the values of their nodes change
    """
    # get the node class
    from p2.calc.Node import Node as node

    # make a probe that records the values of the monitored nodes
    class probe(node.probe):

        def flush(self, observable):
            self.nodes[observable] = observable.getValue()
            return self

        def __init__(self, **kwds):
            super().__init__(**kwds)
            self.nodes = {}
            return

    # make a probe
    p = probe()

    # make a node
    v = 80.
    production = node.variable(value=v)
    assert production.getValue() == v

    # insert the probe
    p.observe(observables=[production])

    # set and check the value
    production.setValue(value=v)
    assert production.getValue() == v
    assert p.nodes[production] == v

    # once more
    v = 100.
    production.setValue(value=v)
    assert production.getValue() == v
    assert p.nodes[production] == v

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
