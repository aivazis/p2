// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// verify that we can instantiate and manipulate inventories


// get the timers
#include <p2/timers.h>
// and the journal
#include <p2/journal.h>

// support
#include <thread>
#include <cassert>
// access the {chrono} literals
using namespace std::literals;

// convenience
using timer_t = pyre::timers::timer_t;


// verify that we can manipulate the timer state
int main() {
    // make a timer
    timer_t timer("tests.timer");
    // and start it
    timer.start();

    // nap duration
    auto nap = 50ms;
    // go to sleep for a bit
    std::this_thread::sleep_for(nap);
    // stop it
    timer.stop();

    // make a channel
    pyre::journal::debug_t channel("pyre.timers");
    // activate it
    channel.activate();
    // and show me
    channel
        << "elapsed time: " << timer.ms()
        << pyre::journal::endl(__HERE__);

    // all done
    return 0;
}


// end of file
