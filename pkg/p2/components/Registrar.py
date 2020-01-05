# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# externals
import weakref


# declaration
class Registrar:
    """
    The managers of protocols, component classes and their instances

    All user defined protocols and components are registered with {Registrar} as they are
    encountered by the framework. Clients can discover the protocol and component classes that
    are registered, the set of instances of any component, as well as the components that
    implement a particular protocol.
    """


    # public data
    protocols = None     # set of known protocols
    components = None    # map of component classes to their instances
    implementers = None  # map of protocols to components that implement them


    # interface
    def registerProtocolClass(self, protocol):
        """
        Register the {protocol} class record
        """
        # add this to the set of known protocols
        self.protocols.add(protocol)
        # initialize the map of its implementors
        self.implementers[protocol] = set()
        # all done
        return protocol


    def registerComponentClass(self, component):
        """
        Register the {component} class record
        """
        # prime the map of components to their instances
        self.components[component] = weakref.WeakSet()

        # go through the pedigree of the component's protocol
        for protocol in component.pyre_protocol.pyre_pedigree:
            # mark component as an implementer of each one
            self.implementers[protocol].add(component)

        # all done
        return component


    # meta methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # the set of known protocols
        self.protocols = set()
        # map: components -> their instances
        self.components = {}
        # map: protocols -> components that implement them
        self.implementers = {}
        # all done
        return


# end of file
