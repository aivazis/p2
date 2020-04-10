// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// exercise the channel manipulators
int main() {
    // make an info channel
    pyre::journal::error_t channel("tests.journal.error");

    // inject nothing
    channel << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
