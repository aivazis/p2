// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Chronicler_h)
#define pyre_journal_Chronicler_h


// singleton that owns the journal default configuration
class pyre::journal::Chronicler {
    // types
public:
    // verbosity level
    using verbosity_type = verbosity_t;
    // global metadata
    using key_type = key_t;
    using value_type = value_t;
    using metadata_type = metadata_t;

    // device support
    using device_type = Device;
    using device_pointer = device_type::pointer_type;

    // interface
public:
    // verbosity
    static inline auto verbosity() -> verbosity_type;
    static inline auto verbosity(verbosity_type) -> verbosity_type;
    // metadata
    static inline auto globals() -> metadata_type &;
    // device support
    static inline auto device() -> device_pointer;
    static inline auto device(device_pointer) -> device_pointer;

    // data members
private:
    static device_pointer _device;
    static metadata_type _globals;
    static verbosity_type _verbosity;

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
