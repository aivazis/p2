// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Error_h)
#define pyre_journal_Error_h


// user facing diagnostic; meant for error messages, i.e. conditions from which the application
// cannot recover
class pyre::journal::Error :
    public Diagnostic<Error>,
    public Channel<Error, Inventory<true>> {
    // types
public:
    using diagnostic_type = Diagnostic<Error>;
    using channel_type = Channel<Error, Inventory<true>>;

    // metamethods
public:
    inline explicit Error(name_type name);

    // interface
public:
    inline void commit();

    // disallow
private:
    Error(const Error &) = delete;
    Error(const Error &&) = delete;
    const Error & operator= (const Error &) = delete;
    const Error & operator= (const Error &&) = delete;
};


// get the inline definitions
#define pyre_journal_Error_icc
#include "Error.icc"
#undef pyre_journal_Error_icc


#endif

// end of file
