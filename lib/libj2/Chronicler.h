// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Chronicler_h)
#define pyre_journal_Chronicler_h


// singleton that own the journal default configuration
class pyre::journal::Chronicler {
    // types
public:
    using device_type = Device;
    using device_pointer = device_type::pointer_type;

    // interface
public:
    // accessor
    static inline auto device() -> device_pointer;
    // mutator
    static inline auto device(device_pointer) -> device_pointer;

    // data members
private:
    static device_pointer _device;

    // disallow
private:
    Chronicler() = delete;
    Chronicler(const Chronicler &) = delete;
    Chronicler(const Chronicler &&) = delete;
    const Chronicler & operator= (const Chronicler &) = delete;
    const Chronicler & operator= (const Chronicler &&) = delete;
};


// get the inline definitions
#define pyre_journal_Chronicler_icc
#include "Chronicler.icc"
#undef pyre_journal_Chronicler_icc


#endif

// end of file
