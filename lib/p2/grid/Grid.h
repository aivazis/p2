// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Grid_h)
#define pyre_grid_Grid_h


template <class packingT, class storageT>
class pyre::grid::Grid {
    // types
public:
    // aliases my template parameters
    using packing_type = packingT;
    using storage_type = storageT;
    // my parts
    using storage_pointer = std::shared_ptr<storage_type>;
    using packing_const_reference = const packing_type &;
    // my value
    using value_type = typename storage_type::cell_type;
    using reference = typename storage_type::reference;
    using const_reference = typename storage_type::const_reference;
    // my shape
    using shape_type = typename packing_type::shape_type;
    using shape_const_reference = const shape_type &;
    // my index
    using index_type = typename packing_type::index_type;
    using index_const_reference = const index_type &;
    // iterators
    using iterator = typename packing_type::index_iterator;

    // metamethods
public:
    constexpr Grid(packing_const_reference, storage_pointer);

    // accessors
public:
    constexpr auto data() const -> storage_pointer;
    constexpr auto layout() const -> packing_const_reference;

    // interface: data access
public:
    constexpr auto operator[](index_const_reference) -> reference;
    constexpr auto operator[](index_const_reference) const -> const_reference;

    // interface: iteration support
public:
    // whole grid iteration: generate a sequence of indices that cover the entire grid in its
    // native packing order
    constexpr auto begin() const;
    constexpr auto end() const;
    // iterate over a portion of the grid
    constexpr auto box(index_const_reference, shape_const_reference) const;

    // slicing: create subgrids of a given shape anchored at the given index; rank reduction is
    // achieved by zeroing out the ranks to be skipped in the shape specification
public:
    template <size_t sliceRank = packing_type::rank()>
    constexpr auto slice(index_const_reference, shape_const_reference);

    // implementation details: data
private:
    const packing_type _layout;
    const storage_pointer _data;

    // default metamethods
public:
    // destructor
    ~Grid() = default;
    // constructors
    Grid(const Grid &) = default;
    Grid(Grid &&) = default;
    Grid & operator=(const Grid &) = default;
    Grid & operator=(Grid &&) = default;
};


// get the inline definitions
#define pyre_grid_Grid_icc
#include "Grid.icc"
#undef pyre_grid_Grid_icc


#endif

// end of file
