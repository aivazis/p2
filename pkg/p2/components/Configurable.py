# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# externals
import itertools


# declaration
class Configurable:
    """
    The base class for components and protocols
    """

    # framework data;
    # names registered with the configuration store
    pyre_name = None           # for instances
    pyre_family = None         # for classes
    # structural
    pyre_pedigree = ()         # ancestors that are configurables, in mro
    pyre_traits = ()           # all traits, both local and inherited
    pyre_localTraits = ()      # traits from my declaration
    pyre_inheritedTraits = ()  # inherited traits
    # name maps
    pyre_namemap = None        # map of trait aliases to their canonical name
    pyre_traitmap = None       # map of canonical trait names to their descriptor
    # convenience
    pyre_locator = None        # the location of the configurable instantiation
    # predicates that avoid runtime type identification
    pyre_isProtocol = False    # am i a protocol?
    pyre_isComponent = False   # am i a component?


    # interface
    @classmethod
    def pyre_trait(cls, alias):
        """
        Given the {alias}, locate and return the associated descriptor
        """
        # attempt to
        try:
            # use the {alias} to retrieve the canonical name
            canonical = cls.pyre_namemap[alias]
        # if this fails, {alias} is not a name for one of my traits
        except KeyError:
            # complain
            raise cls.TraitNotFoundError(configurable=cls, name=alias)

        # got it; attempt to
        try:
            # look through my trait map for the matching descriptor
            trait = cls.pyre_traitmap[canonical]
        # if it's not there
        except KeyError:
            # we have a bug; get the journal
            import journal
            # build a channel
            channel = journal.firewall("pyre.components")
            # and complain
            raise channel.log(f"{cls}: missing trait for '{alias}' -> '{canonical}'")

        # all done
        return trait


    # introspection
    @classmethod
    def pyre_traits(cls):
        """
        Generate a sequence of all my trait descriptors, both locally declared and inherited.

        If you are looking only for traits declared in a particular class, use the attribute
        {cls.pyre_localTraits} instead.
        """
        # the full set of my descriptors is prepared by {Requirement} and separated into two
        # pile: my local traits that were explicitly declared in my class record, and traits i
        # inherited from my ancestors
        return itertools.chain(cls.pyre_localTraits, cls.pyre_inheritedTraits)


    @classmethod
    def pyre_behaviors(cls):
        """
        Generate a sequence of all my trait descriptors that are behaviors
        """
        return filter(lambda trait: trait.isBehavior, cls.pyre_traits())


    @classmethod
    def pyre_derivations(cls):
        """
        Generate a sequence of all my trait descriptors that are derivations
        """
        return filter(lambda trait: trait.isDerivation, cls.pyre_traits())


    @classmethod
    def pyre_measures(cls):
        """
        Generate a sequence of all my trait descriptors that are measures
        """
        return filter(lambda trait: trait.isMeasure, cls.pyre_traits())


    @classmethod
    def pyre_properties(cls):
        """
        Generate a sequence of all my trait descriptors that are properties
        """
        return filter(lambda trait: trait.isProperty, cls.pyre_traits())


    @classmethod
    def pyre_facilities(cls):
        """
        Generate a sequence of all my trait descriptors that are facilities
        """
        return filter(lambda trait: trait.isFacility, cls.pyre_traits())


    @classmethod
    def pyre_localBehaviors(cls):
        """
        Generate a sequence of my local trait descriptors that are behaviors
        """
        return filter(lambda trait: trait.isBehavior, cls.pyre_localTraits)


    @classmethod
    def pyre_localDerivations(cls):
        """
        Generate a sequence of my local trait descriptors that derivations
        """
        return filter(lambda trait: trait.isDerivation, cls.pyre_localTraits)


    @classmethod
    def pyre_localMeasures(cls):
        """
        Generate a sequence of my local trait descriptors that measures
        """
        return filter(lambda trait: trait.isMeasure, cls.pyre_localTraits)


    @classmethod
    def pyre_localProperties(cls):
        """
        Generate a sequence of my local trait descriptors that are properties
        """
        return filter(lambda trait: trait.isProperty, cls.pyre_localTraits)


    @classmethod
    def pyre_localFacilities(cls):
        """
        Generate a sequence of all my trait descriptors that are facilities
        """
        return filter(lambda trait: trait.isFacility, cls.pyre_localTraits)


    @classmethod
    def pyre_inheritedBehaviors(cls):
        """
        Generate a sequence of my inherited trait descriptors that are behaviors
        """
        return filter(lambda trait: trait.isBehavior, cls.pyre_inheritedTraits)


    @classmethod
    def pyre_inheritedDerivations(cls):
        """
        Generate a sequence of my inherited trait descriptors that derivations
        """
        return filter(lambda trait: trait.isDerivation, cls.pyre_inheritedTraits)


    @classmethod
    def pyre_inheritedMeasures(cls):
        """
        Generate a sequence of my inherited trait descriptors that measures
        """
        return filter(lambda trait: trait.isMeasure, cls.pyre_inheritedTraits)


    @classmethod
    def pyre_inheritedProperties(cls):
        """
        Generate a sequence of my inherited trait descriptors that are properties
        """
        return filter(lambda trait: trait.isProperty, cls.pyre_inheritedTraits)


    @classmethod
    def pyre_inheritedFacilities(cls):
        """
        Generate a sequence of all my trait descriptors that are facilities
        """
        return filter(lambda trait: trait.isFacility, cls.pyre_inheritedTraits)


    # framework hooks
    @classmethod
    def pyre_classRegistered(cls):
        """
        Hook that gets invoked by the framework after the class record has been registered but
        before any configuration events
        """
        # do nothing
        return cls


    @classmethod
    def pyre_classConfigured(cls):
        """
        Hook that gets invoked by the framework after the class record has been configured,
        before any instances have been created
        """
        # do nothing
        return cls


    @classmethod
    def pyre_classInitialized(cls):
        """
        Hook that gets invoked by the framework after the class record has been initialized,
        before any instances have been created
        """
        # do nothing
        return cls




# end of file
