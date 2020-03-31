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
    using string_type = std::string;
    using csi_type = CSI;
    using name_type = string_type;
    using color_type = csi_type::rep_type;

    using table_type = std::map<name_type, color_type>;


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
};


#endif

// end of file
