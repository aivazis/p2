// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>


// verify that the debug diagnostic is off by default, and that we can manipulate its state
int main() {
    // make a debug channel
    pyre::journal::debug_t channel("tests.journal.null");

    // if it's active by default
    if (channel) {
        // we have a problem
        throw pyre::journal::firewall_error("active debug channel");
    }

    // attempt to activate
    channel.activate();
    // if it failed to activate
    if (!channel) {
        // we have a problem
        throw pyre::journal::firewall_error("debug channel could not be activated");
    }

    // all done
    return 0;
}


// end of file
