// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Device_h)
#define pyre_journal_Device_h

//
class pyre::journal::Device {
    // types
public:
    using pointer_type = std::shared_ptr<Device>;
    using string_type = std::string;
    using name_type = string_type;
    using entry_type = std::vector<string_type>;
    using key_type = string_type;
    using value_type = string_type;
    using metadata_type = std::map<key_type, value_type>;

    // metamethods
public:
    // constructor
    inline explicit Device(const name_type &);
    // destructor
    virtual ~Device();

    // interface
public:
    // accessor
    inline auto name() const -> const name_type &;

    // abstract
    virtual auto record(const entry_type &, const metadata_type &) -> Device & = 0;

    // data
private:
    name_type _name;
};


// get the inline definitions
#define pyre_journal_Device_icc
#include "Device.icc"
#undef pyre_journal_Device_icc


#endif

// end of file
