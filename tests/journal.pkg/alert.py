#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Exercise the user facing renderer
    """
    # get the renderer
    from j2.Alert import Alert as alert
    # the colospaces
    from j2.ANSI import ANSI
    # and a channel
    from j2.Informational import Informational as info

    # get the chronicler metadata
    gmeta = info.chronicler.notes
    # add some
    gmeta["application"] = "alert"
    gmeta["author"] = "michael"

    # make an info channel
    channel = info(name="tests.journal.info")
    # add some metadata
    channel.notes["time"] = "now"
    channel.notes["device"] = "null"
    # inject
    channel.line("info channel:")
    channel.line("    hello world!")

    # make a palette
    palette = {
        "reset": ANSI.x11("normal"),
        "channel": ANSI.x11("light slate gray"),
        "info": ANSI.x11("steel blue"),
        "body": "",
        }

    # instantiate the renderer
    renderer = alert()
    # ask it to do its thing
    renderer.render(palette=palette, entry=channel.entry)

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
