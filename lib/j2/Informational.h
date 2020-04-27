// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Informational_h)
#define pyre_journal_Informational_h


// user facing channel; meant for informational messages, such as progress reports
class pyre::journal::Informational : public Channel<Informational, InventoryProxy>
{
    // types
public:
    // my parts
    using channel_type = Channel<Informational, InventoryProxy>;
    // my exception
    using exception_type = application_error;

    // metamethods
public:
    inline explicit Informational(const name_type & name, verbosity_type = 1);

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
