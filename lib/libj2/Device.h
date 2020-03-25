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
    using string_t = std::string;
    using entry_t = std::vector<string_t>;
    using metadata_t = std::map<string_t, string_t>;

    // metamethods
public:
    // destructor
    virtual ~Device();

    // interface
public:
    // abstract
    virtual auto record(const entry_t &, const metadata_t &) -> Device & = 0;
};


#endif

// end of file
