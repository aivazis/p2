// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the timers
#include <p2/timers.h>
// support
#include <thread>
#include <cassert>
// access the {chrono} literals
using namespace std::literals;


// type aliases
using proxy_t = pyre::timers::proxy_t;
using index_t = pyre::timers::index_t;


// exercise the timer state index
int main() {
    // make an index
    index_t index;

    // make a movement proxy by looking up a timer name
    proxy_t m1(index.lookup("test.index"));
    // start the movement
    m1.start();
    // it should now be active
    assert (m1.active() == true);

    // nap duration
    auto nap = 50ms;
    // go to sleep for a bit
    std::this_thread::sleep_for(nap);

    // make another proxy to the same movement
    proxy_t m2(index.lookup("test.index"));
    // verify it is running
    assert (m2.active() == true);
    // stop it
    m2.stop();

    // verify that the two timers show the same accumulated time
    assert (m1.read() == m2.read());

    // all done
    return 0;
}


// end of file
