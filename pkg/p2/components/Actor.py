# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# support
from .. import tracking

# superclass
from .Requirement import Requirement


# declaration
class Actor(Requirement):
    """
    The metaclass of components

    {Actor} takes care of all the tasks necessary to convert a component declaration into a
    configurable entity that coöperates fully with the framework
    """


    # types
    from .Role import Role
    from .Inventory import Inventory


    # metamethods
    def __new__(cls, name, bases, attributes, *, family=None, implements=None, **kwds):
        """
        Build a new component record
        """
        # chain up; swallow the locally specified keywords
        component = super().__new__(cls, name, bases, attributes, **kwds)

        # build the protocol specification
        component.pyre_protocol = cls.pyre_buildProtocol(component=component, implements=implements)
        # save the location of the component declaration
        component.pyre_locator = tracking.here(level=1)

        # all done
        return component


    def __init__(self, name, bases, attributes, *, family=None, implements=None, **kwds):
        """
        Initialize a freshly minted component record
        """
        # chain up
        super().__init__(name, bases, attributes, **kwds)

        # if this is an internal component
        if self.pyre_isInternal:
            # there is nothing further to do
            return

        # build the class inventory
        self.pyre_inventory = self.Inventory()

        # all done
        return


    def __setattr__(self, name, value):
        """
        Set the class attribute {name} to {value}
        """
        # we need to override this in order to support setting the values of class traits. left
        # alone, the default implementation would simply override the value of the attribute
        # that holds the descriptor and would disable trait access both classes and instances.

        # N.B.: no need to fret over performance here: class attribute assignment is not
        # something that's expected to happen often

        # during the early phases of component class creation, we set class attributes before
        # the mapping of trait aliases to their canonical names has been set up. recognize
        # these assignments and let them through

        # get my name map
        namemap = self.pyre_namemap
        # so, early enough in the component class setup, or if {name} is not one of my traits
        if namemap is None or name not in namemap:
            # treat like a regular assignment
            return super().__setattr__(name, value)

        # otherwise, get the canonical name
        canonical = namemap[name]
        # get the trait
        trait = self.pyre_traitmap[canonical]
        # add the value to my inventory
        self.pyre_inventory[trait] = value
        # all done
        return


    # implementation details
    @classmethod
    def pyre_buildProtocol(cls, component, implements):
        """
        Build a class that describes the implementation requirements imposed on the {component}
        under construction
        """
        # NYI
        protocols = ()
        # make one and return it
        return cls.Role("protocol", protocols, {}, internal=True)


# end of file
