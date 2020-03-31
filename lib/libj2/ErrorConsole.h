// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// code guard
#if !defined(pyre_journal_ErrorConsole_h)
#define pyre_journal_ErrorConsole_h

// a device that prints to {cout}
class pyre::journal::ErrorConsole : public pyre::journal::stream_t {
    // metamethods
public:
    // constructor
    ErrorConsole();
    // destructor
    virtual ~ErrorConsole();

    // disallow
private:
    ErrorConsole(const ErrorConsole &) = delete;
    ErrorConsole(const ErrorConsole &&) = delete;
    const ErrorConsole & operator= (const ErrorConsole &) = delete;
    const ErrorConsole & operator= (const ErrorConsole &&) = delete;
};


#endif

// end of file
