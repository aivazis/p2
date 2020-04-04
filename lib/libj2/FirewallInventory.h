// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_FirewallInventory_h)
#define pyre_journal_FirewallInventory_h


// the common state shared by all channels of the same name/severity
class pyre::journal::FirewallInventory : public Inventory<true>
{
    // metamethods
public:
    // constructors
    inline explicit FirewallInventory(state_type = true, device_pointer = nullptr);

    // interface
public:
    // accessor
    inline auto fatal() const -> state_type;
    // mutator
    inline state_type fatal(bool);

    // data
private:
    state_type _fatal;

    // disallow
private:
    FirewallInventory(const FirewallInventory &) = delete;
    FirewallInventory(const FirewallInventory &&) = delete;
    const FirewallInventory & operator= (const FirewallInventory &) = delete;
    const FirewallInventory & operator= (const FirewallInventory &&) = delete;
};


// get the inline definitions
#define pyre_journal_FirewallInventory_icc
#include "FirewallInventory.icc"
#undef pyre_journal_FirewallInventory_icc


#endif

// end of file
