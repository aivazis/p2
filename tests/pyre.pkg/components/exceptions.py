#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Tests for all exceptions raised by this package
    """

    # pull the exceptions
    from p2.components.exceptions import ComponentError
    from p2.components.exceptions import CategoryMismatchError
    from p2.components.exceptions import ImplementationSpecificationError
    from p2.components.exceptions import ProtocolNotImplementedError
    from p2.components.exceptions import TraitNotFoundError
    from p2.components.exceptions import FacilitySpecificationError
    from p2.components.exceptions import ProtocolCompatibilityError
    from p2.components.exceptions import ResolutionError
    from p2.components.exceptions import DefaultError
    from p2.components.exceptions import ConfigurationError
    from p2.components.exceptions import InitializationError

    # the base exception
    try:
        # raise it
        raise ComponentError()
    # catch it
    except ComponentError as error:
        # all good
        pass

    # category mismatch
    try:
        # raise it
        raise CategoryMismatchError(configurable=None, target=None, name=None)
    # catch it
    except CategoryMismatchError as error:
        # all good
        pass

    # implementation specification
    try:
        # raise it
        raise ImplementationSpecificationError(component=None, errors=None)
    # catch it
    except ImplementationSpecificationError as error:
        # all good
        pass

    # protocol not implemented correctly
    try:
        # raise it
        raise ProtocolNotImplementedError(component=None, protocol=None, report=None)
    # catch it
    except ProtocolNotImplementedError as error:
        # all good
        pass

    # trait not found
    try:
        # raise it
        raise TraitNotFoundError(configurable=None, name=None)
    # catch it
    except TraitNotFoundError as error:
        # all good
        pass

    # bad facility specification
    try:
        # raise it
        raise FacilitySpecificationError(configurable=None, trait=None, value=None)
    # catch it
    except FacilitySpecificationError as error:
        # all good
        pass

    # protocol compatibility
    try:
        # raise it
        raise ProtocolCompatibilityError(configurable=None, protocol=None)
    # catch it
    except ProtocolCompatibilityError as error:
        # all good
        pass

    # couldn't convert a string into a component
    try:
        # raise it
        raise ResolutionError(protocol=None, value=None, report=None)
    # catch it
    except ResolutionError as error:
        # all good
        pass

    # unknown default value for a facility
    try:
        # raise it
        raise DefaultError(protocol=None)
    # catch it
    except DefaultError as error:
        # all good
        pass

    # bad configuration
    try:
        # raise it
        raise ConfigurationError(configurable=None, errors=[])
    # catch it
    except ConfigurationError as error:
        # all good
        pass

    # bad initialization
    try:
        # raise it
        raise InitializationError(configurable=None, errors=[])
    # catch it
    except InitializationError as error:
        # all good
        pass

    # all done
    return


# main
if __name__ == "__main__":
    # do...
    test()


# end of file
