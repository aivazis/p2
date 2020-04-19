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

    # get the package
    import j2
    # turn it into a journal device
    device = j2.stream(name=filename, stream=ostr)
    # check its name
    assert device.name == filename

    # close the stream
    device.close()

    # get os services
    import os
    # so we can remove the file
    os.unlink(filename)

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
