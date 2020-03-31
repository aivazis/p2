// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>

// support
#include <cassert>


// convenience
using active_t = pyre::journal::inventory_t<true>;
using inactive_t = pyre::journal::inventory_t<false>;

// verify that the default inventory state reflects the compile time settings
// verify that we can manipulate the inventory state at runtime
int main() {
    // make a default inventory
    active_t on;
    // by default, its device is null
    assert(on.device().get() == nullptr);
    // verify the default state is on
    assert(on.defaultState() == true);
    // verify it is on
    assert(on.state() == true);
    // flip it
    on.deactivate();
    // check again
    assert(on.state() == false);

    // make one that is off by default
    inactive_t off;
    // by default, its device is null
    assert(off.device().get() == nullptr);
    // verify the default state is off
    assert(off.defaultState() == false);
    // verify it is off
    assert(off.state() == false);
    // flip it
    off.activate();
    // check again
    assert(off.state() == true);

    // all done
    return 0;
}


// end of file
