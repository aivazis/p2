// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_timers_Index_h)
#define pyre_timers_Index_h


// owner of the map (timer name -> shared movement)
class pyre::timers::Index
{
    // types
public:
    // timer names
    using name_type = name_t;
    // shared movement
    using movement_type = Movement;

    // the map from channel names to movement instances
    using index_type = std::map<name_type, movement_type>;

    // metamethods
public:
    inline Index();
    // let the compiler write the rest
    Index(const Index &) = default;
    Index(Index &&) = default;
    Index & operator= (const Index &) = default;
    Index & operator= (Index &&) = default;

    // interface
public:
    // simple access to the underlying index
    inline auto size() const;
    inline auto empty() const;
    inline auto contains(const name_type &) const;

    // explicit movement insertion
    inline auto emplace(const name_type &);

    // iteration
    inline auto begin() const;
    inline auto end() const;

    // look up the movement of the named timer
    inline auto lookup(const name_type &) -> movement_type &;

    // data members
private:
    index_type _index;
};


// get the inline definitions
#define pyre_timers_Index_icc
#include "Index.icc"
#undef pyre_timers_Index_icc


#endif

// end of file
