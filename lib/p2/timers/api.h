// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_timers_api_h)
#define pyre_timers_api_h


// package api
namespace pyre::timers {
    // wall clock timer
    using wall_timer_t = Timer<WallClock, Proxy>;
}


#endif

// end of file
