// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// type alias
using info_t = pyre::journal::info_t;


// exercise the channel manipulators
int main() {
    // send all channel output to a log file
    info_t::file("info_file.log");

    // make an info channel
    info_t channel("tests.journal.info");

    // inject something into the channel; there should be no output to the screen
    channel
        // location
        << pyre::journal::at(__HERE__)
        // some metadata
        << pyre::journal::note("time", "now")
        // a message with a newline
        << "info channel:" << pyre::journal::newline
        // another message and a flush
        << "    hello world!" << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
