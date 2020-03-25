// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>


// exercise all manipulators
int main() {
    // make a null channel
    pyre::journal::null_t channel("tests.journal.null");

    // inject the manipulators
    channel
        << pyre::journal::at(__HERE__)
        << pyre::journal::set("time", "now")
        << "null channel:" << pyre::journal::newline
        << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
