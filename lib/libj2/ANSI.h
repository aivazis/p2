// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_ANSI_h)
#define pyre_journal_ANSI_h


// a map of color names from known color spaces to the ANSI escape sequences required to render
// them in compatible terminal emulators
class pyre::journal::ANSI {
    // types
public:
    using table_type = colortable_t;

    // static interface
public:
    static bool compatible();

    // static data members
public:
    static table_type null;
    static table_type ansi;
    static table_type x11;
    static table_type gray;
    static table_type misc;

    // implementation details
private:
    static bool _compatible;
};


#endif

// end of file
