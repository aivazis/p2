# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# support
from .. import tracking
from ..framework import priorities

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
    from .ClassInventory import ClassInventory


    # metamethods
    def __new__(cls, name, bases, attributes, *, family=None, implements=None, **kwds):
        """
        Build a new component record
        """
        # chain up; swallow the locally specified keywords
        component = super().__new__(cls, name, bases, attributes, **kwds)

        # if this is an internal class
        if component.pyre_isInternal:
            # go no further
            return component

        # build the protocol specification
        component.pyre_implements = component.pyre_buildProtocol(implements=implements)
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

        # if this is a component that is marked as an implementation detail
        if self.pyre_isInternal:
            # there is nothing further to do
            return

        # build the class inventory
        self.pyre_inventory = self.ClassInventory()

        # all done
        return


    def __call__(self, **kwds):
        # build the instance
        instance = super().__call__(**kwds)
        # and return it
        return instance


    def __setattr__(self, name, value):
        """
        Set the class attribute {name} to {value}
        """
        # we need to override this in order to support setting the values of class traits. left
        # alone, the default implementation would simply overwrite the descriptor with {value},
        # which would disable trait access for both classes and instances.

        # note that during the early phases of component class creation, we set class
        # attributes before the mapping of trait aliases to their canonical names has been set
        # up. such assignments, as well as assignments to attributes not managed by traits, are
        # allowed through

        # get my name map
        namemap = self.pyre_namemap
        # attempt to
        try:
            # look up the canonical name of this attribute
            canonical = namemap[name]
        # early enough in the creation of the component class record, {namemap} is {None}
        except TypeError:
            # so treat this like a regular assignment
            return super().__setattr__(name, value)
        # if the name is not in the {namemap} it must not be a trait
        except KeyError:
            # so treat this like a regular assignment
            return super().__setattr__(name, value)

        # otherwise, get the trait
        trait = self.pyre_traitmap[canonical]
        # build a locator
        locator = tracking.here(level=1)
        # set the priority of this assignment
        priority = priorities.Explicit()
        # get my inventory
        inventory = self.pyre_inventory
        # set the value
        inventory.setValue(component=self, trait=trait, value=value,
                           locator=locator, priority=priority)
        # all done
        return


    # implementation details
    @classmethod
    def pyre_buildProtocol(cls, implements):
        """
        Build a class that describes the implementation requirements imposed on the {component}
        under construction
        """
        # warning
        print("components.Actor.pyre_buildProtocol: NYI!")
        # NYI
        protocols = ()
        # make one and return it
        return cls.Role("protocol", protocols, {}, internal=True)


# end of file
