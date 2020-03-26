// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Inventory_h)
#define pyre_journal_Inventory_h


// the common state shared by all channels of the same name/severity
template <bool stateV>
class pyre::journal::Inventory
{
    // types
public:
    using state_t = bool;
    using device_t = Device;

    // metamethods
public:
    // constructors
    inline explicit Inventory(state_t = stateV, device_t * = nullptr);
    inline Inventory(const Inventory &);
    inline const Inventory & operator= (const Inventory &);

    // interface
public:
    //accessors
    inline auto state() const -> state_t;
    inline auto device() const -> device_t *;

    // mutators
    inline void activate();
    inline void deactivate();
    inline auto device(device_t *) -> device_t *;

    // syntactic sugar
    inline operator bool() const;

    // disallow
private:
    state_t _state;
    device_t * _device;
};


// get the inline definitions
#define pyre_journal_Inventory_icc
#include "Inventory.icc"
#undef pyre_journal_Inventory_icc


#endif

// end of file
