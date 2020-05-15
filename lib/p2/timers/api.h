// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_timers_api_h)
#define pyre_timers_api_h


// end user facing api
namespace pyre::timers {
    // timer
    using timer_t = Timer<Proxy>;
}


// when building or testing
#if defined(PYRE_CORE)
// place these additional symbols in the namespace
namespace pyre::timers {
    // timer parts
    using movement_t = Movement;
    // movement proxy
    using proxy_t = Proxy;
    // timer index
    using index_t = Index;
}
#endif


#endif

// end of file
