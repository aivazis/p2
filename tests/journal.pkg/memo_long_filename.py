#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Exercise the developer facing renderer
    """
    # get the renderer
    from j2.Memo import Memo as memo
    # the color spaces
    from j2.ANSI import ANSI
    # and a channel
    from j2.Debug import Debug as debug

    # make a channel
    channel = debug(name="tests.journal.debug")
    # add a fake stack trace
    channel.notes["filename"] = "a_" + ("very_" * 60) + "long_filename"
    channel.notes["line"] = "30"
    channel.notes["function"] = "test"
    # inject
    channel.line("debug channel:")
    channel.line("    hello from a very long file name")

    # make a palette
    palette = {
        "reset": ANSI.x11("normal"),
        "channel": ANSI.x11("light slate gray"),
        "debug": ANSI.x11("steel blue"),
        "body": "",
        }

    # instantiate the renderer
    renderer = memo()
    # ask it to do its thing
    page = '\n'.join(renderer.render(palette=palette, entry=channel.entry))
    # show me
    # print(page)

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file