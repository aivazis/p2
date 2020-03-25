// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// the package
#include <j2/journal.h>


// exercise the null diagnostic
int main() {
    // make a null channel
    pyre::journal::null_t channel("tests.journal.null");

    // try injecting some text into the channel
    channel
        << pyre::journal::at(__HERE__)
        << pyre::journal::set("time", "now")
        << "null channel:" << pyre::journal::newline
        << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
