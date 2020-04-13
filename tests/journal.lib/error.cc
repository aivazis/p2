// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// alias
using error_t = pyre::journal::error_t;


// verify the basic channel state
int main() {
    // make an error channel
    error_t channel("tests.journal.error");

    // check its name
    assert (channel.name() == "tests.journal.error");
    // by default, it should be active
    assert (channel);
    // and fatal
    assert (channel.fatal());

    // all done
    return 0;
}


// end of file