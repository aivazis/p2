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

    // lookup a couple of names
    index.lookup("test.index.1");
    index.lookup("test.index.2");

    // make sure the index contains two names
    assert (index.size() == 2);
    // and that out names are the ones there
    assert (index.contains("test.index.1"));
    assert (index.contains("test.index.2"));

    // all done
    return 0;
}


// end of file
