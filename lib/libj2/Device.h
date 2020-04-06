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
    // for naming device instances
    using name_type = name_t;
    // the verbosity level
    using verbosity_type = verbosity_t;
    // a page of diagnostics is a vector of lines
    using page_type = page_t;
    // diagnostic metadata in a map
    using key_type = key_t;
    using value_type = value_t;
    using metadata_type = metadata_t;
    // decorators in a map from metadata keys to the colorizer's representation
    using palette_type = palette_t;

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
    virtual auto memo(verbosity_type, const page_type &, const metadata_type &) -> Device & = 0;
    virtual auto alert(verbosity_type, const page_type &, const metadata_type &) -> Device & = 0;

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
