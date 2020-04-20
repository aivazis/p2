#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that we can build a stream based device
    """
    # pick a file name
    filename = "file.out"
    # make a stream
    ostr = open(filename, mode="w")

    # get the device
    from j2.Stream import Stream as stream
    # instantiate
    device = stream(name=filename, stream=ostr)
    # check its name
    assert device.name == filename

    # close the stream; not strictly necessary, but let's exercise the interface
    device.close()

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
