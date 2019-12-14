# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


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
    def __new__(cls, name, bases, attributes, *, internal=False, **kwds):
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
        #
        # N.B.: this must be done carefully to account for trait shadowing where distant
        # ancestor traits become inaccessible when closer ancestors declare a trait with the
        # same name. resist the temptation to speed this up by traversing the pedigree in
        # reverse order and throw everything in the map expecting that closer ancestors will
        # update the maps correctly, because there is no easy way to undo the mapping of the
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

        # record the pedigree
        configurable.pyre_pedigree = pedigree
        # record the trait piles
        configurable.pyre_localTraits = tuple(localTraits)
        configurable.pyre_inheritedTraits = tuple(inheritedTraits)
        # record the name maps
        configurable.pyre_namemap = namemap
        configurable.pyre_traitmap = traitmap
        # mark the visibility of the record
        configurable.pyre_isInternal = internal

        # all done
        return configurable


# end of file
