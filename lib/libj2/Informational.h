// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Informational_h)
#define pyre_journal_Informational_h


// user facing diagnostic; meant for informational messages, such as progress reports
class pyre::journal::Informational :
    public Diagnostic<Informational>,
    public Channel<Informational, Inventory<true>> {
    // types
public:
    using diagnostic_type = Diagnostic<Informational>;
    using channel_type = Channel<Informational, Inventory<true>>;

    // metamethods
public:
    inline explicit Informational(name_type name, verbosity_type = 1);

    // interface
public:
    // record the message in the journal
    inline void commit();

    // disallow
private:
    Informational(const Informational &) = delete;
    Informational(const Informational &&) = delete;
    const Informational & operator= (const Informational &) = delete;
    const Informational & operator= (const Informational &&) = delete;
};


// get the inline definitions
#define pyre_journal_Informational_icc
#include "Informational.icc"
#undef pyre_journal_Informational_icc


#endif

// end of file
