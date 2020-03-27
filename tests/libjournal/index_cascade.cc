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
    auto & parent = index.lookup("test.index.parent");
    // make sure its default state is what we expect
    assert(parent.defaultState() == defaultState);
    // and its actual state is what's expected
    assert(parent.state() == defaultState);
    // turn it off
    parent.deactivate();
    // make sure it happened
    assert(parent.state() == false);

    // lookup a name that's lower in the hierarchy
    auto & child = index.lookup("test.index.parent.blah.blah.child");
    // make sure its default state is what we expect
    assert(child.defaultState() == defaultState);
    // and its actual state is what's expected
    assert(child.state() == parent.state());

    // all done
    return 0;
}


// end of file
