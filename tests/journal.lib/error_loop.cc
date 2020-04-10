// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// type aliases
using myerror_t = pyre::journal::error_t;
using trash_t = pyre::journal::trash_t;


// exercise the channel manipulators
int main() {
    // make an error channel
    myerror_t channel("tests.journal.error");

    // send the output to the trash
    channel.device(std::make_shared<trash_t>());

    // inject repeatedly
    for (auto i=0; i<10; ++i) {
        channel << "i: " << i << pyre::journal::endl;
    }

    // all done
    return 0;
}


// end of file
