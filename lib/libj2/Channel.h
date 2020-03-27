// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Channel_h)
#define pyre_journal_Channel_h

// access to the state shared by all channels of a given severity and name
template <typename severityT>
class pyre::journal::Channel {
    // types
public:
    using string_t = std::string;
    using severity_t = severityT;
    using inventory_t = typename severity_t::inventory_t;
    using state_t = typename inventory_t::state_t;
    using device_t = typename inventory_t::device_t;
    using index_t = Index<inventory_t>;

    // metamethods
public:
    inline explicit Channel(const string_t &);

// syntactic sugar
    inline operator bool() const;

    // interface
public:
    // accessors
    inline auto name() const -> const string_t &;
    inline auto state() const -> state_t;
    inline auto device() const -> device_t *;
    inline static constexpr auto defaultState() -> state_t;

    // mutators
    inline void activate();
    inline void deactivate();
    inline auto device(device_t *) -> device_t *;

    // data members
private:
    string_t _name;
    inventory_t & _inventory;

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
