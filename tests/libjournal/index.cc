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

    // make sure it's empty
    assert(index.empty());

    // all done
    return 0;
}


// end of file
