# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


class PyreError(Exception):
    """
    Base class for all pyre related errors
    """

    # public data
    description = "generic pyre error"

    # metamethods
    def __init__(self, description=None, locator=None, **kwds):
        # chain up
        super().__init__(**kwds)
        # attach the locator
        self.locator = locator
        # check whether we have to attach a special error description
        if description is not None: self.description = description
        # all done
        return

    def __str__(self):
        # render the error message
        reason = self.description.format(self)
        # if we have a locator
        if self.locator:
            # give it a chance to pinpoint the error
            return f"{self.locator}: {reason}"
        # otherwise
        return reason


class FrameworkError(PyreError):
    """
    Base class for all framework exceptions

    Useful when you are trying to catch any and all pyre framework errors
    """


class BadResourceLocatorError(FrameworkError):
    """
    Exception raised when a URI is not formed properly
    """

    # public data
    description = "{0.uri}: {0.reason}"

    # metamethods
    def __init__(self, uri, reason, **kwds):
        # chain up
        super().__init__(**kwds)
        # store the error info
        self.uri = uri
        self.reason = reason
        # all done
        return


class ComponentNotFoundError(FrameworkError):

    # public data
    description = "could not resolve {0.uri} into a component"

    # public data
    def __init__(self, uri, **kwds):
        # chain up
        super().__init__(**kwds)
        # store the error info
        self.uri = uri
        # all done
        return


class ExternalNotFoundError(FrameworkError):
    """
    Base class for parsing errors
    """

    # public data
    description = "could not locate support for external package {0.category!r}"

    # metamethods
    def __init__(self, category, **kwds):
        # chain up
        super().__init__(**kwds)
        # store the error info
        self.category = category
        # all done
        return


# end of file
