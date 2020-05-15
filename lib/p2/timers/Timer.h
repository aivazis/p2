// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_timers_Timer_h)
#define pyre_timers_Timer_h


// user facing encapsulation of a timer
template <class proxyT>
class pyre::timers::Timer : public proxyT {
    // types
public:
    // my registry
    using index_type = Index;
    // my name
    using name_type = index_type::name_type;

    // metamethods
public:
    // constructor
    inline explicit Timer(const name_type &);
    // let the compiler write the destructor
    ~Timer() = default;

    // accessors
public:
    inline auto name() const;

    // implementation details: data members
private:
    name_type _name;

    // implementation details: static data
private:
    // the timer registry
    static index_type _registry;

    // disable constructors and assignments
private:
    Timer(const Timer &) = delete;
    Timer(Timer &&) = delete;
    Timer & operator=(const Timer &) = delete;
    Timer & operator=(Timer &&) = delete;
};


// get the inline definitions
#define pyre_timers_Timer_icc
#include "Timer.icc"
#undef pyre_timers_Timer_icc


#endif

// end of file
