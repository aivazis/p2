// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// type alias
using warning_t = pyre::journal::warning_t;


// send all output to a log file
int main() {
    // send all channel output to a log file
    warning_t::logfile("warning_file.log");

    // make a warning channel
    warning_t channel("tests.journal.warning");

    // inject something into the channel; there should be no output to the screen
    channel
        // location
        << pyre::journal::at(__HERE__)
        // some metadata
        << pyre::journal::note("time", "now")
        // a message with a newline
        << "warning channel:" << pyre::journal::newline
        // another message and a flush
        << "    hello world!" << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
