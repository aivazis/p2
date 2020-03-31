// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Channel_h)
#define pyre_journal_Channel_h


// access to the state shared by all channels of a given severity and name
// do not be tempted to remove the {severityT} template parameter: its presence is essential in
// order to guarantee that each channel category gets its own static data, such as the channel
// {_index}
template <typename severityT, typename inventoryT>
class pyre::journal::Channel {
    // types
public:
    using severity_type = severityT;
    using inventory_type = inventoryT;
    using state_type = typename inventory_type::state_type;
    using index_type = Index<inventory_type>;
    using name_type = typename index_type::name_type;

    // metamethods
public:
    inline explicit Channel(const name_type &);

// syntactic sugar
    inline operator bool() const;

    // interface
public:
    // accessors
    inline auto name() const -> const name_type &;
    inline auto state() const -> state_type;
    inline auto inventory() const -> inventory_type &;

    // mutators
    inline void activate();
    inline void deactivate();

    // static interface
public:
    // accessors
    inline static auto index() -> const index_type &;
    inline static constexpr auto defaultState() -> state_type;

    // inventory access
    inline static auto lookup(const name_type &) -> inventory_type &;

    // data members
private:
    name_type _name;              // my name
    inventory_type & _inventory;  // my shared state

    // static data
private:
    static index_type _index;     // the index that holds all channels of this severity

    // disallow
private:
    Channel(const Channel &) = delete;
    Channel(const Channel &&) = delete;
    const Channel & operator= (const Channel &) = delete;
    const Channel & operator= (const Channel &&) = delete;
};


// get the inline definitions
#define pyre_journal_Channel_icc
#include "Channel.icc"
#undef pyre_journal_Channel_icc


#endif

// end of file
