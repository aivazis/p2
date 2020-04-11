// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>

// support
#include <cassert>


// convenience
using inventory_t = pyre::journal::error_t::inventory_type;

// verify that we can manipulate the error inventory state
int main() {
    // make a default inventory
    inventory_t error;
    // by default, its device is null
    assert(error.device().get() == nullptr);

    // verify the default state is on
    assert(error.defaultState() == true);
    // verify it is on
    assert(error.state() == true);
    // flip it
    error.deactivate();
    // check again
    assert(error.state() == false);

    // verify it's fatal by default
    assert(error.fatal() == true);
    // flip it
    error.fatal(false);
    // check again
    assert(error.fatal() == false);

    // all done
    return 0;
}


// end of file
