// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Selector_h)
#define pyre_journal_Selector_h


// selectors are channel manipulators that decorate channels with metadata
class pyre::journal::Selector
{
    // types
public:
    using string_type = std::string;
    using key_type = string_type;
    using value_type = string_type;

    // metamethods
public:
    // constructor
    inline Selector(key_type, value_type);

    // interface
public:
    template <typename channelT>
    inline auto
    inject(channelT &) const -> channelT &;

    // data
private:
    key_type _key;
    value_type _value;
};


// get the inline definitions
#define pyre_journal_Selector_icc
#include "Selector.icc"
#undef pyre_journal_Selector_icc


#endif

// end of file
