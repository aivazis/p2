# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# superclass
from ..patterns.AttributeFilter import AttributeFilter


# declaration
class Requirement(AttributeFilter):
    """
    Metaclass that captures the class record processing that is common to both protocols and
    components
    """


    # types
    from ..traits.Trait import Trait
    from .Configurable import Configurable


    # metamethods
    def __new__(cls, name, bases, attributes, *, family=None, **kwds):
        """
        Build the class record for a new configurable
        """
        # build the record
        configurable = super().__new__(cls, name, bases, attributes, **kwds)

        # compute the pedigree
        pedigree = tuple(base for base in configurable.mro()
                         if issubclass(base, cls.Configurable) and base is not cls.Configurable)

        # initialize storage for the name maps
        namemap = {}  # aliases -> canonical name
        traitmap = {} # canonical name -> descriptor
        # initialize the trait piles
        localTraits = []     # declared in the record we are building
        inheritedTraits = [] # inherited from all ancestors

        # scan the attributes for traits
        for name, trait in cls.pyre_harvest(attributes=attributes, descriptor=cls.Trait):
            # map the name to the trait
            traitmap[name] = trait
            # map all aliases to the canonical name; this includes the canonical name since
            # trait binding happens during the creation of the class record
            namemap.update((alias, name) for alias in trait.aliases)
            # add the trait to the local pile
            localTraits.append(trait)

        # scan my ancestors for traits
        # N.B.: this must be done carefully to account for trait shadowing where distant
        # ancestor traits become inaccessible when closer ancestors declare a trait with the
        # same name. resist the temptation to speed this up by traversing the pedigree in
        # reverse order and throw everything in the map expecting that closer ancestors will
        # update the maps correctly: there is no obvious easy way to undo the mapping of the
        # aliases of a trait that get shadowed by a closer ancestor
        for base in pedigree[1:]:
            # and through each trait
            for trait in base.pyre_localTraits:
                # get the name of the trait
                traitName = trait.name
                # and its aliases
                traitAliases = trait.aliases
                # if the name is not shadowed
                if traitName not in traitmap:
                    # add it to the pile
                    inheritedTraits.append(trait)
                    # map its canonical name
                    traitmap[traitName] = trait
                    # go through its aliases
                    for traitAlias in traitAliases:
                        # if there is no existing entry
                        if traitAlias not in namemap:
                            # map the alias to the canonical name
                            namemap[traitAlias] = traitName

        # record the public name; for class records {pyre_name} and {pyre_family} are identical
        configurable.pyre_name = family
        configurable.pyre_family = family
        # record the pedigree
        configurable.pyre_pedigree = pedigree
        # record the trait piles
        configurable.pyre_localTraits = tuple(localTraits)
        configurable.pyre_inheritedTraits = tuple(inheritedTraits)
        # record the name maps
        configurable.pyre_namemap = namemap
        configurable.pyre_traitmap = traitmap

        # all done
        return configurable


    # type checks
    # N.B.: these are used by {Actor} during the creation of the protocol a component
    # implements. components and protocols themselves are marked as such at creation time, so
    # if you already know that an object is one of these, you can check the {pyre_isComponent}
    # or {pyre_isProtocol} to distinguish them. {Actor} has a slightly different problem: it
    # has to filter out base classes that are not components, and detect non-protocols among
    # the {implements} specification by the user. hence the more careful implementation here
    @classmethod
    def pyre_isComponent(cls, candidate):
        """
        Check whether {candidate} is a component class
        """
        # attempt to
        try:
            # ask it
            flag = candidate.pyre_isComponent
        # if it doesn't know
        except AttributeError:
            # it isn't
            flag = False
        # return with the answer
        return flag


    @classmethod
    def pyre_isProtocol(cls, candidate):
        """
        Check whether {candidate} is a protocol class
        """
        # attempt to
        try:
            # ask it
            flag = candidate.pyre_isProtocol
        # if it doesn't know
        except AttributeError:
            # it isn't
            flag = False
        # return with the answer
        return flag


# end of file
