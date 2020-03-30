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
    using string_type = std::string;

    // global metadata
    using key_type = string_type;
    using value_type = string_type;
    using metadata_type = std::map<key_type, value_type>;

    // device support
    using device_type = Device;
    using device_pointer = device_type::pointer_type;

    // interface
public:
    // metadata
    static inline auto globals() -> metadata_type &;

    // device support
    static inline auto device() -> device_pointer;
    static inline auto device(device_pointer) -> device_pointer;

    // data members
private:
    static device_pointer _device;
    static metadata_type _globals;

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
