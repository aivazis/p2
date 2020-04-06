// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Debug_h)
#define pyre_journal_Debug_h


// developer facing diagnostic; usually gets turned off in release mode
class pyre::journal::Debug :
    public Diagnostic<Debug>,
    public Channel<Debug, Inventory<false>> {
    // types
public:
    using diagnostic_type = Diagnostic<Debug>;
    using channel_type = Channel<Debug, Inventory<false>>;
    using nameset_type = nameset_t;

    // metamethods
public:
    inline explicit Debug(name_type name);

    // interface
public:
    // record the message in the journal
    inline void commit();

    // initialize the channel index
    static inline auto initializeIndex() -> index_type;
    // bulk channelactivation
    static inline void activateChannels(const nameset_type &);

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
