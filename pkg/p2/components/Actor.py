# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# externals
import itertools
import collections.abc
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
    from .exceptions import ImplementationSpecificationError


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

        # get the class inventory factory
        from .ClassInventory import ClassInventory
        # make one and attach it
        self.pyre_inventory = ClassInventory()

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
    def pyre_buildProtocol(cls, component, implements):
        """
        Build a class that describes the implementation requirements imposed on the {component}
        under construction
        """
        # get the base protocol; it is equivalent to an empty specification
        from .Protocol import Protocol

        # if nothing was provided
        if implements is None:
            # i don't have a protocol specification
            mine = ()
        # if i got a single protocol
        elif cls.pyre_isProtocol(implements):
            # make a pile with only one entry
            mine = implements,
        # if i got an iterable of protocols
        elif isinstance(implements, collections.abc.Iterable):
            # go through the contents and collect the entries that are not protocols
            foreign = tuple(itertools.filterfalse(cls.pyre_isProtocol, implements))
            # if there were any
            if foreign:
                # complain
                raise cls.ImplementationSpecificationError(component=component, errors=foreign)
            # if every entry was a protocol, put them on a pile
            mine = tuple(implements)
        # anything else
        else:
            # is an error
            raise cls.ImplementationSpecificationError(component=component, errors=implements)

        # now, collect the commitments made by my immediate ancestors
        inherited = tuple(
            base.pyre_protocol
            for base in component.__bases__
            if cls.pyre_isComponent(base) and base.pyre_protocol is not Protocol)

        # assemble the full pile
        bases = mine + inherited
        # if it is empty
        if len(bases) == 0:
            # use it directly
            return Protocol
        # if there is only one protocol on the pile
        if len(bases) == 1:
            # just return it
            return bases[0]

        # otherwise, we must construct one; get the protocol metaclass
        from .Role import Role
        # make one
        protocol =  Role("protocol", bases, {})
        # mark it as mine, since python doesn't get this right just yet
        protocol.__module__ = component.__module__

        # and return it
        return protocol


# end of file
