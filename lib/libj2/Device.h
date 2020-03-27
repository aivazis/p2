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
    using string_type = std::string;
    using entry_type = std::vector<string_type>;
    using metadata_type = std::map<string_type, string_type>;

    // metamethods
public:
    // destructor
    virtual ~Device();

    // interface
public:
    // abstract
    virtual auto record(const entry_type &, const metadata_type &) -> Device & = 0;
};


#endif

// end of file
