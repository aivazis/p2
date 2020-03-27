// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Locator_h)
#define pyre_journal_Locator_h


// the locator diagnostic conforms to the API but has no effect
class pyre::journal::Locator
{
    // types
public:
    using string_type = std::string;

    // metamethods
public:
    // constructor
    inline explicit Locator(const char * = "", int = 0, const char * = "");

    // interface
public:
    template <typename channelT>
    inline auto
    inject(channelT &) const -> channelT &;

    // data
private:
    string_type _file;
    string_type _line;
    string_type _func;
};


// get the inline definitions
#define pyre_journal_Locator_icc
#include "Locator.icc"
#undef pyre_journal_Locator_icc


#endif

// end of file
