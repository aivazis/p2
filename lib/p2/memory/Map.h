// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_Map_h)
#define pyre_memory_Map_h


// a file-backed block of cells
template <class cellT>
class pyre::memory::Map : public FileMap {
    // types
public:
    // my cell
    using cell_type = cellT;
    // derived types
    using pointer = cell_type *;
    using reference = cell_type &;
    using const_pointer = const cell_type *;
    using const_reference = const cell_type &;

    // metamethods
public:
    // map an existing data product
    inline explicit Map(uri_type, writable_type = false);
    // create a new one, given a path and a number of cells
    inline explicit Map(uri_type, size_type);

    // interface
public:
    inline auto cells() const;
    inline auto data() const;

    // disallow
private:
    Map(const Map &) = delete;
    Map(const Map &&) = delete;
    const Map & operator= (const Map &) = delete;
    const Map & operator= (const Map &&) = delete;
};


// get the inline definitions
#define pyre_memory_Map_icc
#include "Map.icc"
#undef pyre_memory_Map_icc


# endif

// end of file
