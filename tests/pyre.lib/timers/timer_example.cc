// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the timers
#include <p2/timers.h>
#include <p2/journal.h>
// support
#include <thread>
#include <cassert>
// access the {chrono} literals
using namespace std::literals;


// type aliases
using timer_t = pyre::timers::timer_t;


// verify that two timers that have the same name share the same movement
int main() {
    // make a timer
    timer_t t("tests.timer");
    // start it
    t.start();

    // nap duration
    auto nap = 50ms;
    // go to sleep for a bit
    std::this_thread::sleep_for(nap);

    // stop the timer
    t.stop();

    // make a channel
    pyre::journal::debug_t channel("tests.timer");
    // activate it
    channel.activate();
    // show me
    channel
        << "elapsed time: " << t.us()
        << pyre::journal::endl(__HERE__);

    // all done
    return 0;
}


// end of file
