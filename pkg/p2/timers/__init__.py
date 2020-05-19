# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2020 all rights reserved
#


"""
This package provides the necessary infrastructure for timing applications.

The sequence

    import pyre
    t = pyre.timers.wall(name="test")
    t.start()
    .
    .
    .
    t.stop()
    elapsed = t.read()

produces a timer, and registers it under the name {test}. Timers must be started before any
readings can take place. Stopping a timer prevents it from accumulating time, while {t.read}
returns the total amount of time the timer has been active. Timers can be {reset} and
reused as many times as you like.

Another interesting feature is that registered timers are available from anywhere in an
application. You can register a timer in one place, access it and start it in another, and stop
it and take a reading in a third, all without needing to pass around the variable. The timer
registry grants access to the same timer when it is asked for a timer of known name.

If the {libpyre} bindings are available, you are sharing these timers with low level code as
well.
"""


# end of file
