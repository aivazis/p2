// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Selector_h)
#define pyre_journal_Selector_h


// the selector diagnostic conforms to the API but has no effect
class pyre::journal::Selector
{
    // types
public:
    using string_t = std::string;

    // metamethods
public:
    // constructor
    inline Selector(string_t, string_t);

    // interface
public:
    template <typename channelT>
    inline auto
    inject(channelT &) const -> channelT &;

    // data
private:
    string_t _key;
    string_t _value;
};


// get the inline definitions
#define pyre_journal_Selector_icc
#include "Selector.icc"
#undef pyre_journal_Selector_icc


#endif

// end of file
