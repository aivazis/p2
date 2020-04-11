// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Fatal_h)
#define pyre_journal_Fatal_h


// the common state shared by all channels of the same name/severity
template <bool fatalV, bool stateV>
class pyre::journal::Fatal : public Inventory<stateV>
{
    // types
public:
    using state_type = typename Inventory<stateV>::state_type;
    using device_type = typename Inventory<stateV>::device_type;
    using device_pointer = typename Inventory<stateV>::device_pointer;

    // metamethods
public:
    // constructors
    inline explicit Fatal(state_type = fatalV, state_type = stateV, device_pointer = nullptr);

    // let the compiler write the others
    Fatal(const Fatal &) = default;
    Fatal(Fatal &&) = default;
    Fatal & operator= (const Fatal &) = default;
    Fatal & operator= (Fatal &&) = default;

    // interface
public:
    // accessor
    inline auto fatal() const -> state_type;
    // mutator
    inline state_type fatal(bool);

    // data
private:
    state_type _fatal;
};


// get the inline definitions
#define pyre_journal_Fatal_icc
#include "Fatal.icc"
#undef pyre_journal_Fatal_icc


#endif

// end of file
