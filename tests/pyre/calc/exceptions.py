#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify the interface of all the exceptions raised by this package
    """

    # get the package exceptions
    from p2.calc.exceptions import (
        EvaluationError,
        EmptyExpressionError, ExpressionSyntaxError, UnresolvedNodeError,
        AliasingError)

    try:
        raise EvaluationError(node=None, error=None)
    except EvaluationError as error:
        pass

    try:
        raise EmptyExpressionError(expression=None, normalized=None)
    except EmptyExpressionError as error:
        pass

    try:
        raise ExpressionSyntaxError(expression=None, error=None)
    except ExpressionSyntaxError as error:
        pass

    try:
        raise UnresolvedNodeError(node=None, name=None)
    except UnresolvedNodeError as error:
        pass

    try:
        raise AliasingError(key=None, target=None, alias=None,
                            targetNode=None, targetInfo=None, aliasNode=None, aliasInfo=None)
    except AliasingError as error:
        pass

    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
