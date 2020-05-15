// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the timers
#include <p2/timers.h>
// support
#include <cassert>


// type aliases
using index_t = pyre::timers::index_t;


// exercise the timer state index
int main() {
    // make an index
    index_t index;

    // lookup a name
    auto & movement = index.lookup("test.index");
    // make sure its activation state is what we expect
    assert(movement.active() == false);

    // all done
    return 0;
}


// end of file
