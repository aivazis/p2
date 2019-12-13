#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


def test():
    """
    Verify that the {__get__} methods works as expected
    """

    # get the descriptor class
    from p2.descriptors.Descriptor import Descriptor as descriptor


    # make a subclass
    class trait(descriptor):

        # that implements the protocol
        def __get__(self, instance, cls):
            # if i'm invoked a class attribute
            if instance is None:
                # return the class
                return cls
            # otherwise, return the instance
            return instance


    # make a client
    class Client:

        raw = descriptor()
        cooked = trait()

    # verify that
    try:
        # access of the base descriptor raises an error
        Client.raw
        # so we shouldn't get here
        assert False, "unreachable"
    # trap the expected failure
    except NotImplementedError:
        # and ignore it; all good
        pass

    # access the functional descriptor; the result should be the class record
    assert Client.cooked is Client

    # instantiate and repeat
    client = Client()

    # first the bas descriptor
    try:
        # this should raise an error
        client.raw
        # so we shouldn't get here
        assert False, "unreachable"
    # trap the expected failure
    except NotImplementedError:
        # and ignore it; all good
        pass

    # access the functional descriptor; the result should be the instance
    assert client.cooked is client

    # all done
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
