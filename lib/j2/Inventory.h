// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Inventory_h)
#define pyre_journal_Inventory_h


// the state shared by all channels of a given name+severity
class pyre::journal::Inventory {
    // types
public:
    using active_type = bool;
    using fatal_type = bool;
    using device_type = device_ptr;

    // metamethods
public:
    inline explicit Inventory(active_type = true, fatal_type = false);

    // accessors
public:
    inline auto active() const;
    inline auto fatal() const;
    inline auto device() const;

    // mutators
public:
    inline auto active(active_type) -> Inventory &;
    inline auto fatal(fatal_type) -> Inventory &;
    inline auto device(device_type) -> Inventory &;

    // syntactic sugar
public:
    inline operator active_type() const;

    // data members
private:
    active_type _active;
    fatal_type  _fatal;
    device_type _device;
};


// get the inline definitions
#define pyre_journal_Inventory_icc
#include "Inventory.icc"
#undef pyre_journal_Inventory_icc


#endif

// end of file
