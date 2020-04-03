// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Trash_h)
#define pyre_journal_Trash_h


// a device that ignores all requests for output
class pyre::journal::Trash : public pyre::journal::Device {
    // metamethods
public:
    // constructor
    inline Trash();
    // destructor
    virtual ~Trash();

    // interface
public:
    // developer diagnostics
    virtual auto memo(const entry_type &, const metadata_type &) -> Trash &;
    // user facing diagnostics
    virtual auto alert(const entry_type &, const metadata_type &) -> Trash &;

    // disallow
private:
    Trash(const Trash &) = delete;
    Trash(const Trash &&) = delete;
    const Trash & operator= (const Trash &) = delete;
    const Trash & operator= (const Trash &&) = delete;
};


// get the inline definitions
#define pyre_journal_Trash_icc
#include "Trash.icc"
#undef pyre_journal_Trash_icc


#endif

// end of file
