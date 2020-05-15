// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// verify that we can instantiate and manipulate inventories


// get the timers
#include <p2/timers.h>

// support
#include <cassert>


// convenience
using movement_t = pyre::timers::movement_t;


// verify that we can manipulate the movement state
int main() {
    // make a movement
    movement_t movement;

    // verify it is inactive, by default
    assert (movement.active() == false);

    // all done
    return 0;
}


// end of file
