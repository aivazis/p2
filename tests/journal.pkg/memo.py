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
    # the colospaces
    from j2.ANSI import ANSI
    # and a channel
    from j2.Debug import Debug as debug

    # get the chronicler metadata
    gmeta = debug.chronicler.meta
    # add some
    gmeta["application"] = "memo"
    gmeta["author"] = "michael"

    # make a channel
    channel = debug(name="tests.journal.debug")
    # add some metadata
    channel.meta["time"] = "now"
    channel.meta["device"] = "null"
    # inject
    channel.line("debug channel:")
    channel.line("    hello world!")

    # make a palette
    palette = {
        "reset": ANSI.x11("normal"),
        "channel": ANSI.x11("light slate gray"),
        "debug": ANSI.x11("steel blue"),
        "body": "",
        }

    # extract the page from the channel
    page = channel.page
    # and the metadata
    meta = channel.meta

    # instantiate the renderer
    renderer = memo()
    # ask it to do its thing
    renderer.render(palette=palette, page=page, meta=meta)

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
