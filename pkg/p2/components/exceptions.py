# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


"""
Definitions for all exceptions raised by this package
"""


# get the base exception
from ..framework.exceptions import FrameworkError


# build a local base so we have a catch all
class ComponentError(FrameworkError):
    """
    Base class for all component specification errors
    """

class CategoryMismatchError(ComponentError):
    """
    Exception raised when two configurables have traits by the same name but have different
    categories
    """

    # public data
    description = "category mismatch in trait {0.name!r} between {0.configurable} and {0.target}"

    # metamethods
    def __init__(self, configurable, target, name, **kwds):
        # chain up
        super().__init__(**kwds)
        # save the error info
        self.configurable = configurable
        self.target = target
        self.name = name
        # all done
        return


class ImplementationSpecificationError(ComponentError):
    """
    Exception raised when the {implements} specification of a component declaration contains
    errors, e.g. classes that don't derive from {Protocol}
    """

    # public data
    description = '{0.component} has a poorly formed implementation specification'

    # metamethods
    def __init__(self, component, errors, **kwds):
        # chain up
        super().__init__(**kwds)
        # save the error info
        self.component = component
        self.errors = errors
        # all done
        return


class ProtocolNotImplementedError(ComponentError):
    """
    Exception raised when a component does not implement correctly the protocols in its
    implementation specification
    """

    # public data
    description = '{0.component} does not implement {0.protocol} correctly'

    # metamethods
    def __init__(self, component, protocol, report, **kwds):
        # chain up
        super().__init__(**kwds)
        # and record the error conditions for whomever may be catching this exception
        self.component = component
        self.protocol = protocol
        self.report = report
        # all done
        return


class TraitNotFoundError(ComponentError):
    """
    Exception raised when a request for a trait fails
    """

    # public data
    description = "{0.configurable} has no trait named {0.name!r}"

    # metamethods
    def __init__(self, configurable, name, **kwds):
        # pass it on
        super().__init__(**kwds)
        # save the source of the error
        self.configurable = configurable
        self.name = name
        # all done
        return


class FacilitySpecificationError(ComponentError):
    """
    Exception raised when a facility cannot instantiate its configuration specification
    """

    # public data
    description = "{0.__name__}.{0.trait.name}: could not instantiate {0.value!r}"

    # metamethods
    def __init__(self, configurable, trait, value, **kwds):
        # chain up
        super().__init__(**kwds)
        # save the error info

        self.configurable = configurable
        self.trait = trait
        self.value = value
        # all done
        return


class ProtocolCompatibilityError(ComponentError):
    """
    Exception raised when a configurable is incompatible with a suggested protocol
    """

    # public data
    description = '{0.configurable} is incompatible with {0.protocol}'

    # metamethods
    def __init__(self, configurable, protocol, **kwds):
        # chain up
        super().__init__(**kwds)
        # store my context
        self.configurable = configurable
        self.protocol = protocol
        # all done
        return


class ResolutionError(ComponentError):
    """
    Exception raised when a protocol cannot resolve a string into a component
    """

    # public data
    description = 'could not resolve {0.value!r} into a component that implements {0.protocol}'

    # metamethods
    def __init__(self, protocol, value, report=None, **kwds):
        # chain up
        super().__init__(**kwds)
        # store my context
        self.protocol = protocol
        self.value = value
        self.report = report
        # all done
        return


class DefaultError(ComponentError):
    """
    Exception raised when a protocol cannot determine a valid default value
    """

    # public data
    description = 'no valid default binding for {0.protocol}'

    # metamethods
    def __init__(self, protocol, **kwds):
        # chain up
        super().__init__(**kwds)
        # store my context
        self.protocol = protocol
        # all done
        return


class ConfigurationError(ComponentError):
    """
    Exception raised when something bad happens during component configuration
    """

    # public data
    description = 'while configuring {0.configurable}:\n    {0.report}'

    @property
    def report(self):
        """
        Splice my errors together
        """
        return "\n    ".join(map(str, self.errors))

    # metamethods
    def __init__(self, configurable, errors, **kwds):
        # chain up
        super().__init__(**kwds)
        # store my context
        self.configurable = configurable
        self.errors = errors
        # all done
        return


class InitializationError(ComponentError):
    """
    Exception raised when something bad happens during component initialization
    """

    # public data
    description = 'while initializing {0.configurable}:\n    {0.report}'

    @property
    def report(self):
        """
        Splice my errors together
        """
        return "\n    ".join(map(str, self.errors))

    # metamethods
    def __init__(self, configurable, errors, **kwds):
        # chain up
        super().__init__(**kwds)
        # store my context
        self.configurable = configurable
        self.errors = errors
        # all done
        return


# end of file
