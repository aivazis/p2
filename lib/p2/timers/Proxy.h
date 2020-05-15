// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_timers_Proxy_h)
#define pyre_timers_Proxy_h


// proxy for accessing a timer movement on behalf of a client
class pyre::timers::Proxy {
    // types
public:
    // my object
    using movement_type = Movement;
    using movement_reference = movement_type &;
    // its parts
    using active_type = movement_type::active_type;
    using duration_type = movement_type::duration_type;
    using time_point_type = movement_type::time_point_type;

    // metamethods
public:
    inline explicit Proxy(movement_reference);

    // accessors
public:
    // ask whether the movement is active
    inline auto active() const;
    // get the timestamp of last activation
    inline auto mark() const;

    // interface
public:
    // buttons
    inline auto start();
    inline auto stop();
    inline auto reset() -> movement_reference;

    // readouts
    // get the accumulated time; make sure to stop the timer first, otherwise the behavior is
    // undefined
    inline auto read() const ;
    // compute the accumulated time without disturbing the timer;
    inline auto lap() const;

    // display convenience
    // read the accumulated time and render it as a string in seconds
    inline auto sec() const;
    // read the accumulated time and render it as a string in milliseconds
    inline auto ms() const;
    // read the accumulated time and render it as a string in microseconds
    inline auto us() const;

    // syntactic sugar
public:
    inline operator active_type() const;

    // other meta-methods: let the compiler write these
public:
    // constructors and assignments
    Proxy(const Proxy &) = delete;
    Proxy(Proxy &&) = delete;
    Proxy & operator=(const Proxy &) = delete;
    Proxy & operator=(Proxy &&) = delete;
    // destructor
    ~Proxy() = default;

    // data member
private:
    movement_reference _movement;
};


// get the inline definitions
#define pyre_timers_Proxy_icc
#include "Proxy.icc"
#undef pyre_timers_Proxy_icc


#endif

// end of file
