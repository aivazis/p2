// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>


// exercise the null diagnostic
int main() {
    // make a null channel
    pyre::journal::null_t channel("tests.journal.null");

    // try injecting some text into the channel
    channel << "    Hello world!";

    // all done
    return 0;
}


// end of file
