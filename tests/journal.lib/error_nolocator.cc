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
    // make an error channel
    pyre::journal::error_t channel("tests.journal.error");

    // send the output to the trash
    channel.device(std::make_shared<pyre::journal::trash_t>());

    // do not provide location information
    channel
        << "an error message without location information"
        << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
