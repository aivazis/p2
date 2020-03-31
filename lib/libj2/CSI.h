// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_CSI_h)
#define pyre_journal_CSI_h


//
class pyre::journal::CSI {
    // types
public:
    using string_type = std::string;

    // static interface
public:
    // the old 3 bit colors: {code} in [30,37] or [40,47]
    inline static auto csi3(int code, bool bright=false) -> string_type;
    // 8 bit color: values in [0,7]
    inline static auto csi8(int red, int green, int blue, bool foreground=true) -> string_type;
    inline static auto csi8_gray(int gray, bool foreground=true) -> string_type;
    // 24 bit color: values in [0,23]
    inline static auto csi24(int red, int green, int blue, bool foreground=true) -> string_type;
    // turn blink on and off; there isn't wide support for this, so avoid it
    inline static auto blink(bool state=true) -> string_type;

    // static data members
private:
    static const string_type esc;
};


// get the inline definitions
#define pyre_journal_CSI_icc
#include "CSI.icc"
#undef pyre_journal_CSI_icc


#endif

// end of file
