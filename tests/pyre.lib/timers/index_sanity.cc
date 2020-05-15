// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the timers
#include <p2/timers.h>
// support
#include <cassert>


// type alias
using index_t = pyre::timers::index_t;


// verify that the timer state index can be instantiated
int main() {
    // make an index
    index_t index;

    // make sure it's empty
    assert(index.empty());

    // all done
    return 0;
}


// end of file
