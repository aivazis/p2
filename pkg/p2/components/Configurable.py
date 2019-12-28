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


    # types
    from .exceptions import TraitNotFoundError
    from .exceptions import CategoryMismatchError


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
            # so complain
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
        # piles: my local traits that were explicitly declared in my class record, and traits i
        # inherited from my ancestors
        return itertools.chain(cls.pyre_localTraits, cls.pyre_inheritedTraits)


    @classmethod
    def pyre_behaviors(cls):
        """
        Generate a sequence of my trait descriptors that are behaviors
        """
        # go through my traits, looking for behaviors
        return filter(lambda trait: trait.isBehavior, cls.pyre_traits())


    @classmethod
    def pyre_derivations(cls):
        """
        Generate a sequence of my trait descriptors that are derivations
        """
        # go through my traits, looking for derivations
        return filter(lambda trait: trait.isDerivation, cls.pyre_traits())


    @classmethod
    def pyre_measures(cls):
        """
        Generate a sequence of my trait descriptors that are measures
        """
        # go through my traits, looking for measures
        return filter(lambda trait: trait.isMeasure, cls.pyre_traits())


    @classmethod
    def pyre_properties(cls):
        """
        Generate a sequence of my trait descriptors that are properties
        """
        # go through my traits, looking for properties
        return filter(lambda trait: trait.isProperty, cls.pyre_traits())


    @classmethod
    def pyre_facilities(cls):
        """
        Generate a sequence of my trait descriptors that are facilities
        """
        # go through my traits, looking for facilities
        return filter(lambda trait: trait.isFacility, cls.pyre_traits())


    @classmethod
    def pyre_localBehaviors(cls):
        """
        Generate a sequence of my local trait descriptors that are behaviors
        """
        # go through my traits, looking for behaviors that were declared locally
        return filter(lambda trait: trait.isBehavior, cls.pyre_localTraits)


    @classmethod
    def pyre_localDerivations(cls):
        """
        Generate a sequence of my local trait descriptors that are derivations
        """
        # go through my traits, looking for derivations that were declared locally
        return filter(lambda trait: trait.isDerivation, cls.pyre_localTraits)


    @classmethod
    def pyre_localMeasures(cls):
        """
        Generate a sequence of my local trait descriptors that are measures
        """
        # go through my traits, looking for measures that were declared locally
        return filter(lambda trait: trait.isMeasure, cls.pyre_localTraits)


    @classmethod
    def pyre_localProperties(cls):
        """
        Generate a sequence of my local trait descriptors that are properties
        """
        # go through my traits, looking for properties that were declared locally
        return filter(lambda trait: trait.isProperty, cls.pyre_localTraits)


    @classmethod
    def pyre_localFacilities(cls):
        """
        Generate a sequence of my local trait descriptors that are facilities
        """
        # go through my traits, looking for facilities that were declared locally
        return filter(lambda trait: trait.isFacility, cls.pyre_localTraits)


    @classmethod
    def pyre_inheritedBehaviors(cls):
        """
        Generate a sequence of my inherited trait descriptors that are behaviors
        """
        # go through my traits, looking for inherited behaviors
        return filter(lambda trait: trait.isBehavior, cls.pyre_inheritedTraits)


    @classmethod
    def pyre_inheritedDerivations(cls):
        """
        Generate a sequence of my inherited trait descriptors that are derivations
        """
        # go through my traits, looking for inherited derivations
        return filter(lambda trait: trait.isDerivation, cls.pyre_inheritedTraits)


    @classmethod
    def pyre_inheritedMeasures(cls):
        """
        Generate a sequence of my inherited trait descriptors that are measures
        """
        # go through my traits, looking for inherited measures
        return filter(lambda trait: trait.isMeasure, cls.pyre_inheritedTraits)


    @classmethod
    def pyre_inheritedProperties(cls):
        """
        Generate a sequence of my inherited trait descriptors that are properties
        """
        # go through my traits, looking for inherited properties
        return filter(lambda trait: trait.isProperty, cls.pyre_inheritedTraits)


    @classmethod
    def pyre_inheritedFacilities(cls):
        """
        Generate a sequence of my inherited trait descriptors that are facilities
        """
        # go through my traits, looking for inherited facilities
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


    # compatibility check
    @classmethod
    def pyre_isCompatible(cls, spec, fast=True):
        """
        Check whether {cls} is assignment compatible with {spec}.

        In typical use, {cls} is a component and {spec} is either a protocol or another
        component.

        Here, we confine ourselves to the part of the problem that involves assignment
        compatibility, i.e. whether {cls} provides all the traits specified by {spec}. Further
        constraints may be provided by {Configurable} subclasses.

        If {fast} is {True}, this method will return as soon as it discovers the first
        incompatibility, without performing an exhaustive check of all traits. If you are
        interested in the full set of incompatibilities, pass {False} to get a detailed
        compatibility report
        """
        # get the report factory
        from .CompatibilityReport import CompatibilityReport
        # initialize
        report = CompatibilityReport(component=cls, specification=spec)

        # go through the traits in {spec}
        for hers in spec.pyre_traits():
            # get its name
            name = hers.name
            # if i have a trait by this name
            try:
                # grab it
                mine = cls.pyre_traitmap[name]
            # if i don't
            except KeyError:
                # build an error description
                error = cls.TraitNotFoundError(configurable=cls, name=name)
                # add it to the report
                report.incompatibilities[hers].append(error)
                # if we are in fast mode
                if fast:
                    # bail
                    return report
                # otherwise grab the next trait
                continue

            # so i have a trait by this name; if it's not the right kind
            if not issubclass(type(mine), type(hers)):
                #  build an error description
                error = cls.CategoryMismatchError(configurable=cls, target=spec, name=name)
                # add it to the report
                report.incompatibilities[hers].append(error)
                # if we are in fast mode
                if fast:
                    # bail
                    return report
                # otherwise, grab the next trait
                # N.B.: the superfluous {continue} is here in case more checking is added below
                continue

        # all done
        return report


# end of file
