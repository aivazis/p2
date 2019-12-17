#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


def test():
    """
    Verify that the priority ordering is correct
    """
    # externals
    import random
    # access
    from p2.framework.priorities import Priority as priority

    # the names of the categories, in rank order
    names = [
        "uninitialized",
        "defaults",
        "boot",
        "package",
        "persistent",
        "user",
        "command",
        "explicit",
        "framework",
        ]

    # create an instance of each one
    priorities = tuple(
        # get the class and invoke the constructor
        getattr(priority, name)()
        # for each name in my list
        for name in names )

    # first check that when the ranks are all equal, the priorities rank correctly
    # scramble and sort
    target = tuple(sorted(random.sample(priorities, k=len(priorities))))
    # check that it is exactly what we started with
    assert priorities == target

    # adjust the ranks in reverse order and repeat
    for p in priorities:
        # set the rank
        p.rank = len(priorities) - p.category
    # scramble and sort
    target = tuple(sorted(random.sample(priorities, k=len(priorities))))
    # check that it is exactly what we started with
    assert priorities == target

    # all done
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    test()


# end of file
