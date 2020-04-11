// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// verify that everything works correctly in the absence of location information
int main() {
    // make an info channel
    pyre::journal::debug_t channel("tests.journal.debug");

    // turn it on
    channel.activate();
    // but send the output to the trash
    channel.device(std::make_shared<pyre::journal::trash_t>());

    // do not provide location information
    channel
        << "a debug message without location information"
        << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
