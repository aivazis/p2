# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# attempt to
try:
    # the journal bindings
    from . import p2 as libpyre
# if something goes wrong
except ImportError:
    # mark; the rest of the package will adjust
    libpyre = None


# end of file
