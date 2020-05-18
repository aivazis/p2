// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// verify that we can instantiate and manipulate inventories


// get the timers
#include <p2/timers.h>

// support
#include <thread>
#include <cassert>
// access the {chrono} literals
using namespace std::literals;

// convenience
using timer_t = pyre::timers::process_timer_t;


// verify that we can manipulate the timer state
int main() {
    // make a timer
    timer_t timer("tests.timer");
    // and start it
    timer.start();

    // do something
    double sum=0;
    for (int i=0; i < 1000*1000; ++i) {
        sum += i;
    }

    // stop it
    timer.stop();

    // reset the timer
    timer.reset();
    // verify it is inactive
    assert (timer.active() == false);
    // and that the accumulated time is reset to zero
    assert (timer.read() == timer_t::duration_type::zero());

    // all done
    return 0;
}


// end of file
