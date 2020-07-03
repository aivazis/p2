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
    // my index
    using index_type = typename packing_type::index_type;
    using index_const_reference = const index_type &;

    // metamethods
public:
    constexpr Grid(packing_const_reference, storage_pointer);

    // interface: data access
public:
    constexpr auto operator[](index_const_reference) -> reference;
    constexpr auto operator[](index_const_reference) const -> const_reference;

    // implementation details: data
private:
    storage_pointer _data;
    const packing_type _layout;

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
