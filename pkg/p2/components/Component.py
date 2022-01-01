# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# superclass
from .Configurable import Configurable
# metaclass
from .Actor import Actor
# the base protocol
from .Protocol import Protocol


# declaration
class Component(Configurable, metaclass=Actor):
    """
    The base class for all components
    """


    # types
    from .exceptions import ProtocolCompatibilityError


    # framework data
    # structural
    pyre_inventory = None    # trait value management
    pyre_protocol = Protocol # my default protocol; overwritten by {Actor} during construction
    # type id
    pyre_isComponent = True


    # metamethods
    def __init__(self, name=None, **kwds):
        # chain up
        super().__init__(**kwds)
        # save my name
        self.pyre_name = name
        # all done
        return


    def __str__(self):
        """
        Build a human readable representation
        """
        # accumulator of the name fragments
        fragments = []

        # get my name
        name = self.pyre_name
        # if i have one
        if name is not None:
            # use it
            fragments.append(f"component '{name}'")
        # otherwise
        else:
            # mark the component a s private
            fragments.append("unnamed component")

        # get my family name
        family = self.pyre_family
        # if i have one
        if family is not None:
            # use it
            fragments.append(f"an instance of '{family}'")
        # otherwise
        else:
            # get my class name and use it
            fragments.append(f"an instance of '{type(self).__name__}'")

        # assemble and return
        return ", ".join(fragments)


    # implementation details
    @classmethod
    def pyre_isCompatibleWith(cls, spec, fast=True):
        """
        Check whether {cls} is compatible with {spec}
        """
        # chain up to perform the basic checks
        report = super().pyre_isCompatibleWith(spec=spec, fast=fast)
        # if we found an incompatibility and we are not interested in the details
        if fast and not report.isClean:
            # nothing further to do
            return report

        # if {spec} is not a protocol
        if not spec.pyre_isProtocol:
            # we don't have anything further to do for component-component checks
            return report

        # grab my protocol
        mine = cls.pyre_protocol
        # check that {spec} is type compatible with it
        if not mine.pyre_isTypeCompatibleWith(protocol=spec):
            # build an error descriptor
            error = cls.ProtocolCompatibilityError(configurable=cls, protocol=spec)
            # add it to the report
            report.incompatibilities[spec].append(error)
            # if we are in fast mode
            if fast:
                # do nothing further
                return report

        # all done
        return report


# end of file
