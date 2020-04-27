// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Debug_h)
#define pyre_journal_Debug_h


// developer facing channel; usually gets turned off in release mode
class pyre::journal::Debug : public Channel<Debug, InventoryProxy>
{
    // types
public:
    // my parts
    using channel_type = Channel<Debug, InventoryProxy>;
    // my exception
    using exception_type = debug_error;

    // metamethods
public:
    inline Debug(const name_type &, verbosity_type = 1);

    // implementation details; don't access directly
public:
    // record the message in the journal
    inline void record();
    // raise an exception when fatal
    inline void die();

    // static methods
public:
    // initialize the channel index
    static inline auto initializeIndex() -> index_type;

    // disallow
private:
    Debug(const Debug &) = delete;
    Debug(const Debug &&) = delete;
    const Debug & operator= (const Debug &) = delete;
    const Debug & operator= (const Debug &&) = delete;
};


// get the inline definitions
#define pyre_journal_Debug_icc
#include "Debug.icc"
#undef pyre_journal_Debug_icc


#endif

// end of file
