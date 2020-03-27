// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>
#include <iostream>


// type aliases
const bool defaultState = true;
using index_t = pyre::journal::index_t<pyre::journal::inventory_t<defaultState>>;


// exercise the channel state index
int main() {
    // make an index
    index_t index;

    // lookup a name
    index.lookup("test.index.1");
    // and another one
    index.lookup("test.index.2");

    // initialize the count
    std::size_t count = 0;
    // go through the contents
    for (auto & item : index) {
        // get the inventory
        auto & inventory = item.second;
        // verify the channel state is as expected
        assert(inventory.state() == inventory.defaultState());
        // increment the counter
        count++;
    }
    // verify that we went through all the channels
    assert(count == index.size());

    // all done
    return 0;
}


// end of file
