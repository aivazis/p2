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
    filename = "file_sanity.log"

    # get the device
    from j2.File import File
    # instantiate
    device = File(path=filename)

    # check its name
    assert device.name == "log"
    # and the path
    assert device.path == filename

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
