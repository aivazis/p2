// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// make sure empty injections into a warning work as expected
int main() {
    // make an info channel
    pyre::journal::warning_t channel("tests.journal.warning");

    // inject nothing
    channel << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
