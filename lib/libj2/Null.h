// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Null_h)
#define pyre_journal_Null_h


// the null diagnostic conforms to the API but has no effect
class pyre::journal::Null
{
    // types
public:
    using string_t = std::string;

    // metamethods
public:
    // constructor
    inline explicit Null(const string_t &);

    // syntactic sugar
    inline constexpr operator bool() const;

    // interface
public:
    // state management
    inline void activate() const;
    inline void deactivate() const;

    // disallow
private:
    Null(const Null &) = delete;
    Null(const Null &&) = delete;
    const Null & operator= (const Null &) = delete;
    const Null & operator= (const Null &&) = delete;
};


// get the inline definitions
#define pyre_journal_Null_icc
#include "Null.icc"
#undef pyre_journal_Null_icc


#endif

// end of file
