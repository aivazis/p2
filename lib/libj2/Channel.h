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
    using string_type = std::string;
    using severity_type = severityT;
    using inventory_type = typename severity_type::inventory_type;
    using state_type = typename inventory_type::state_type;
    using index_type = index_t<inventory_type>;

    // metamethods
public:
    inline explicit Channel(const string_type &);

// syntactic sugar
    inline operator bool() const;

    // interface
public:
    // accessors
    inline auto name() const -> const string_type &;
    inline auto state() const -> state_type;
    inline static constexpr auto defaultState() -> state_type;

    // mutators
    inline void activate();
    inline void deactivate();

    // data members
private:
    string_type _name;
    inventory_type & _inventory;

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
