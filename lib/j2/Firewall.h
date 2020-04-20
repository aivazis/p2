// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Firewall_h)
#define pyre_journal_Firewall_h


// developer facing diagnostic; usually gets turned off in release mode
class pyre::journal::Firewall :
    public Diagnostic<Firewall>,
    public Channel<Firewall, Fatal<true, true>> {
    // types
public:
    // my parts
    using diagnostic_type = Diagnostic<Firewall>;
    using channel_type = Channel<Firewall, Fatal<true, true>>;
    // the error indicator
    using exception_type = firewall_error;

    // metamethods
public:
    inline explicit Firewall(const name_type &, verbosity_type = 1);

    // interface
public:
    // control over whether firewalls are fatal
    inline auto fatal() -> state_type;
    inline auto fatal(state_type) -> state_type;
    // commit the message to a device
    inline void commit();

    // disallow
private:
    Firewall(const Firewall &) = delete;
    Firewall(const Firewall &&) = delete;
    const Firewall & operator= (const Firewall &) = delete;
    const Firewall & operator= (const Firewall &&) = delete;
};


// get the inline definitions
#define pyre_journal_Firewall_icc
#include "Firewall.icc"
#undef pyre_journal_Firewall_icc


#endif

// end of file
