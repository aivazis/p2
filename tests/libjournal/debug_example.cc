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
    // make a debug channel
    pyre::journal::debug_t channel("tests.journal.debug");

    // activate the channel
    // channel.activate();

    // inject something into the channel
    channel
        << pyre::journal::at(__HERE__)
        << pyre::journal::set("time", "now")
        << "debug channel:" << pyre::journal::newline
        << "    hello world!" << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
