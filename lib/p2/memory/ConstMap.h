// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_ConstMap_h)
#define pyre_memory_ConstMap_h


// a file-backed block of cells
template <class T, bool checkBounds>
class pyre::memory::ConstMap : public FileMap {
    // types
public:
    // my cell
    using value_type = T;
    // derived types
    using pointer = const value_type *;
    using reference = const value_type &;
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
    inline explicit ConstMap(uri_type);

    // interface
public:
    inline auto cells() const;
    inline auto data() const;

    // iterator support
    inline auto begin() const -> const_pointer;
    inline auto end() const -> const_pointer;

    // syntactic sugar: data access
    inline auto operator[](size_type) const -> const_reference;

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
