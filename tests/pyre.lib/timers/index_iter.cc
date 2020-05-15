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


// exercise iterating through the index contents
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
    for (auto & [name, movement] : index) {
        // verify the timer activation state is as expected
        assert(movement.active() == false);
        // increment the counter
        count++;
    }
    // verify that we went through all the timers
    assert(count == index.size());

    // all done
    return 0;
}


// end of file
