// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Firewall_h)
#define pyre_journal_Firewall_h


// developer facing channel; usually gets turned off in release mode
class pyre::journal::Firewall : public Channel<Firewall, InventoryProxy>
{
    // types
public:
    // my parts
    using channel_type = Channel<Firewall, InventoryProxy>;
    // my exception
    using exception_type = firewall_error;

    // metamethods
public:
    inline explicit Firewall(const name_type &, verbosity_type = 1);

    // implementation details
public:
    // record the message to a device
    inline void record();
    // raise the correct exception when fatal
    inline void die();

    // implementation details
public:
    // initialize the channel index
    static inline auto initializeIndex() -> index_type;

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
