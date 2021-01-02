#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Verify that the category rankings have been recorded correctly
    """
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

    # go through them
    for category, name in enumerate(names):
        # retrieve the priority category
        cls = getattr(priority, name)
        # check the name
        assert cls.name == name, (
            f"name mismatch: expected '{name}', got '{cls.name}'")
        # and the rank; don't forget priorities start with {uninitialized} at -1
        assert cls.category == category-1, (
            f"category mismatch: expected {category-1}, got {cls.category}")

    # all done
    return


# main
if __name__ == "__main__":
    # do...
    test()


# end of file
