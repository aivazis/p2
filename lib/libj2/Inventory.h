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
    using state_type = bool;
    using device_type = Device;

    // metamethods
public:
    // constructors
    inline explicit Inventory(state_type = stateV, device_type * = nullptr);

    // syntactic sugar
    inline operator bool() const;

    // interface
public:
    // accessors
    inline auto state() const -> state_type;
    inline auto device() const -> device_type *;
    inline static constexpr auto defaultState() -> state_type;

    // mutators
    inline void activate();
    inline void deactivate();
    inline auto device(device_type *) -> device_type *;

    // data
private:
    state_type _state;
    device_type * _device;

    // disallow
private:
    Inventory(const Inventory &) = delete;
    Inventory(const Inventory &&) = delete;
    const Inventory & operator= (const Inventory &) = delete;
    const Inventory & operator= (const Inventory &&) = delete;
};


// get the inline definitions
#define pyre_journal_Inventory_icc
#include "Inventory.icc"
#undef pyre_journal_Inventory_icc


#endif

// end of file
