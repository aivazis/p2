// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Warning_h)
#define pyre_journal_Warning_h


// user facing diagnostic; meant for warning messages, i.e. when the applications detects
// something wrong but it can work around the problem
class pyre::journal::Warning :
    public Diagnostic<Warning>,
    public Channel<Warning, Inventory<true>> {
    // types
public:
    using diagnostic_type = Diagnostic<Warning>;
    using channel_type = Channel<Warning, Inventory<true>>;

    // metamethods
public:
    inline explicit Warning(name_type name);

    // interface
public:
    inline void commit();

    // disallow
private:
    Warning(const Warning &) = delete;
    Warning(const Warning &&) = delete;
    const Warning & operator= (const Warning &) = delete;
    const Warning & operator= (const Warning &&) = delete;
};


// get the inline definitions
#define pyre_journal_Warning_icc
#include "Warning.icc"
#undef pyre_journal_Warning_icc


#endif

// end of file
