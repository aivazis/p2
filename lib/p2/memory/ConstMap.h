// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_ConstMap_h)
#define pyre_memory_ConstMap_h


// a file-backed block of cells
template <class cellT>
class pyre::memory::ConstMap : public FileMap {
    // types
public:
    // my cell
    using cell_type = cellT;
    // derived types
    using pointer = const cell_type *;
    using reference = const cell_type &;
    using const_pointer = const cell_type *;
    using const_reference = const cell_type &;

    // metamethods
public:
    // map an existing data product
    inline explicit ConstMap(uri_type);

    // interface
public:
    inline auto cells() const;
    inline auto data() const;

    // disallow
private:
    ConstMap(const ConstMap &) = delete;
    ConstMap(const ConstMap &&) = delete;
    const ConstMap & operator= (const ConstMap &) = delete;
    const ConstMap & operator= (const ConstMap &&) = delete;
};


// get the inline definitions
#define pyre_memory_ConstMap_icc
#include "ConstMap.icc"
#undef pyre_memory_ConstMap_icc


# endif

// end of file
