// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// code guard
#if !defined(pyre_journal_Console_h)
#define pyre_journal_Console_h

// a device that prints to {cout}
class pyre::journal::Console : public pyre::journal::stream_t {
    // metamethods
public:
    // constructor
    Console();
    // destructor
    virtual ~Console();

    // interface
public:
    inline bool tty() const;

    // data
private:
    bool _tty;

    // disallow
private:
    Console(const Console &) = delete;
    Console(const Console &&) = delete;
    const Console & operator= (const Console &) = delete;
    const Console & operator= (const Console &&) = delete;
};


// get the inline definitions
#define pyre_journal_Console_icc
#include "Console.icc"
#undef pyre_journal_Diagnostic_icc


#endif

// end of file