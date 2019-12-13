#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


def test():
    # get the descriptor class
    from p2.descriptors.DataDescriptor import DataDescriptor as descriptor


    # make a subclass
    class trait(descriptor):

        # that implements the protocol
        def __get__(self, instance, cls):
            # if this instance access
            if instance is not None:
                # retrieve the value from the {instance} inventory
                return instance.inventory[self]
            # otherwise, just return myself
            return self


        def __set__(self, instance, value):
            # store {value} in the {instance} inventory
            instance.inventory[self] = value
            # all done
            return self


    # make a client
    class Client:

        raw = descriptor()
        cooked = trait()

        # meta methods
        def __init__(self, **kwds):
            # chain up
            super().__init__(**kwds)
            # initialize my inventory
            self.inventory = {}
            # all done
            return


    # instantiate
    client = Client()

    # first set the value of the base descriptor
    try:
        # this should raise an error
        client.raw = 5
        # so we shouldn't get here
        assert False, "unreachable"
    # trap the expected failure
    except AttributeError as error:
        # unpack the arguments
        desc, instance = error.args
        # verify that the instance is correct
        assert instance is client

    # access the functional descriptor before we ever set its value
    try:
        # the lookup is expected to fail
        client.cooked
    # so trap it
    except KeyError as error:
        # get the key that cause the lookup to fail
        key, *_ = error.args
        # verify it's the trait we accessed
        assert key == Client.cooked

    # set the value
    client.cooked = True
    # and check
    assert client.cooked is True

    # all done
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
