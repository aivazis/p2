// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Device_h)
#define pyre_journal_Device_h


// the base class of all journal devices
class pyre::journal::Device {
    // types
public:
    // pointers to me
    using pointer_type = std::shared_ptr<Device>;
    // alias of the basic string type
    using string_type = std::string;
    // for naming device instances
    using name_type = string_type;
    // a diagnostic entry is a vector of lines
    using entry_type = std::vector<string_type>;
    // diagnostic metadata in a map
    using key_type = string_type;
    using value_type = string_type;
    using metadata_type = std::map<key_type, value_type>;
    // decorators in a map from metadata keys to the colorizer's representation
    using palette_type = std::map<key_type, CSI::rep_type>;

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
