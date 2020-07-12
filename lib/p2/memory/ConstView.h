// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_ConstView_h)
#define pyre_memory_ConstView_h


// a block of cells whose memory is owned by someone else
template <class T>
class pyre::memory::ConstView {
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
    inline ConstView(pointer, cell_count_type);

    // interface
public:
    // the number of cells
    inline auto cells() const;
    // the memory footprint of the block
    inline auto bytes() const;
    // access to the raw data pointer
    inline auto data() const;

    // iterator support
    inline auto begin() const -> pointer;
    inline auto end() const -> pointer;

    // data access
    // with bounds checking
    inline auto at(size_type) const -> const_reference;
    // without bounds checking
    inline auto operator[](size_type) const -> const_reference;

    // implementation details: data
private:
    pointer _data;
    cell_count_type _cells;

    // disallow
private:
    ConstView(const ConstView &) = delete;
    ConstView(const ConstView &&) = delete;
    const ConstView & operator= (const ConstView &) = delete;
    const ConstView & operator= (const ConstView &&) = delete;
};


// get the inline definitions
#define pyre_memory_ConstView_icc
#include "ConstView.icc"
#undef pyre_memory_ConstView_icc


# endif

// end of file
