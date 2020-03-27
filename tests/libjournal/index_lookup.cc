// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>


// type aliases
const bool defaultState = true;
using index_t = pyre::journal::index_t<pyre::journal::inventory_t<defaultState>>;


// exercise the channel state index
int main() {
    // make an index
    index_t index;

    // lookup a name
    auto & inventory = index.lookup("test.index");
    // make sure its default state is what we expect
    assert(inventory.defaultState() == defaultState);
    // and its actual state is what's expected
    assert(inventory.state() == defaultState);
    // turn it off
    inventory.deactivate();
    // make sure it happened
    assert(inventory.state() == false);

    // all done
    return 0;
}


// end of file
