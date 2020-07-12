// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_Map_h)
#define pyre_memory_Map_h


// a file-backed block of cells
template <class T>
class pyre::memory::Map : public FileMap {
    // types
public:
    // my cell
    using value_type = T;
    // derived types
    using pointer = value_type *;
    using reference = value_type &;
    using const_pointer = const value_type *;
    using const_reference = const value_type &;

    // distances
    using difference_type = std::ptrdiff_t;

    // sizes of things
    using size_type = size_t;
    using cell_count_type = size_type;

    // metamethods
public:
    // map an existing data product
    inline explicit Map(uri_type, writable_type = false);
    // create a new one, given a path and a number of cells
    inline explicit Map(uri_type, size_type);

    // interface
public:
    // the number of cells; the inherited {bytes} tells you the memory footprint of the block
    inline auto cells() const;
    // access to the raw data pointer
    inline auto data() const;

    // iterator support
    inline auto begin() -> pointer;
    inline auto end() -> pointer;

    // data access
public:
    // with bounds checking
    inline auto at(size_type) -> reference;
    inline auto at(size_type) const -> const_reference;
    // without bounds checking
    inline auto operator[](size_type) -> reference;
    inline auto operator[](size_type) const -> const_reference;

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
