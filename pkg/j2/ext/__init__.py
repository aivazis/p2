# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# attempt to
try:
    # load the journal bindings
    from . import j2 as libjournal
# if something goes wrong
except ImportError:
    # mark; the rest of the package will adjust
    libjournal = None


# end of file
