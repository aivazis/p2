// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_View_h)
#define pyre_memory_View_h


// a block of cells whose memory belongs to someone else
template <class cellT, bool checkBounds>
class pyre::memory::View {
    // types
public:
    // my cell
    using cell_type = cellT;
    // derived types
    using pointer = cell_type *;
    using reference = cell_type &;
    using const_pointer = const cell_type *;
    using const_reference = const cell_type &;

    // sizes of things
    using size_type = size_t;
    using cell_count_type = size_type;

    // metamethods
public:
    // destructor
    inline ~View() = default;
    // map an existing data product
    inline View(pointer, cell_count_type);

    // interface
public:
    // the number of cells
    inline auto cells() const;
    // the memory footprint of the block
    inline auto bytes() const;
    // access to the raw data pointer
    inline auto data() const;

    // iterator support
    inline auto begin() -> pointer;
    inline auto end() -> pointer;

    // syntactic sugar: data access
    inline auto operator[](size_type) -> reference;
    inline auto operator[](size_type) const -> const_reference;

    // implementation details: data
private:
    pointer _data;
    cell_count_type _cells;

    // disallow
private:
    View(const View &) = delete;
    View(const View &&) = delete;
    const View & operator= (const View &) = delete;
    const View & operator= (const View &&) = delete;
};


// get the inline definitions
#define pyre_memory_View_icc
#include "View.icc"
#undef pyre_memory_View_icc


# endif

// end of file
