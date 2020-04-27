// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_InventoryProxy_h)
#define pyre_journal_InventoryProxy_h


// proxy for accessing inventory values on behalf of a client
template <typename clientT>
class pyre::journal::InventoryProxy {
    // types
public:
    // my client
    using client_type = clientT;
    using client_reference = clientT&;
    // my object
    using inventory_type = Inventory;
    using inventory_reference = inventory_type&;
    // its parts
    using active_type = inventory_type::active_type;
    using fatal_type = inventory_type::fatal_type;
    using device_type = inventory_type::device_type;

    // metamethods
public:
    inline explicit InventoryProxy(inventory_reference inventory);

    // accessors
public:
    inline auto active() const;
    inline auto fatal() const;
    inline auto device() const;

    // mutators
public:
    inline auto active(active_type) -> client_reference;
    inline auto fatal(fatal_type) -> client_reference;
    inline auto device(device_type) -> client_reference;

    // syntactic sugar
public:
    inline operator active_type() const;

    // data members
private:
    inventory_reference _inventory;
};


// get the inline definitions
#define pyre_journal_InventoryProxy_icc
#include "InventoryProxy.icc"
#undef pyre_journal_InventoryProxy_icc


#endif

// end of file
