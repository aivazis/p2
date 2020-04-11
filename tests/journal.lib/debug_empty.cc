// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// verify that empty messages are handled correctly
int main() {
    // make an info channel
    pyre::journal::debug_t channel("tests.journal.debug");

    // turn it on
    channel.activate();
    // inject nothing
    channel << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
