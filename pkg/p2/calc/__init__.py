# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


"""
This package provides the implementation of a simple evaluation network.

There are three fundamental abstractions: variables, operators, and literals. Variables hold
the values computed by the evaluation network, operators compute their values by acting on the
values of other nodes, and literals encapsulate foreign objects, such as numeric constants.
These abstractions provide the machinery for representing arbitrary expressions as graphs.

The interesting aspect of this package is that nodal values get updated automatically when the
values of any of the nodes in their domain change. Nodes keep track of the set of dependents
that are interested in their values and post notifications when their values change.

In addition, this package provides {SymbolTable}, a simple manager for evaluation nodes. Beyond
node storage, {SymbolTable} enables the naming of nodes and can act as the name resolution
context for {Expression} nodes, which evaluate strings with arbitrary python expressions that
may involve the values of other nodes in the model. The other nodes provided here operate
independently of {SymbolTable}. However, it is a good idea to build some kind of container to
hold nodes while the evaluation graph is in use.

Simple examples of the use of the ideas in this package are provided in the unit tests. For a
somewhat more advanced example, take a look at {pyre.config.Configurator}, which is a
{Hierarchical} model that builds an evaluation network out of the traits of pyre components, so
that trait settings can refer to the values of other traits in the configuration files.
"""


# debugging support; see the top level {__init__} file for instructions on how to enable this
def debug():
    """
    Enable debugging for this package: we replace the {Node} metaclass with an extent aware
    version to make sure that all instances are garbage collected
    """
    # get support
    from ..patterns.Extent import Extent
    # access the normal metaclass
    global calculator

    # use it to derive a new one
    class counted(calculator, Extent):
        """
        A creator of extent aware {calc} nodes
        """

    # attach it
    calculator = counted

    # all done
    return


# end of file
