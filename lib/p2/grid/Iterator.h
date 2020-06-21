// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Iterator_h)
#define pyre_grid_Iterator_h


// iterators generate sequences of indices from a packing strategy according to a specific
// order
template <class packingT>
class pyre::grid::Iterator {
    // types
public:
    // my template parameter
    using packing_type = packingT;
    // alias for me
    using iterator_type = Iterator<packing_type>;
    // my parts
    using index_type = typename packing_type::index_type;
    using shape_type = typename packing_type::shape_type;
    using order_type = typename packing_type::order_type;

    // metamethods
public:
    // destructor
    ~Iterator() = default;

    // constructor
    constexpr Iterator(index_type, shape_type, order_type);
    // let the compiler write the rest
    constexpr Iterator(const Iterator &) = default;
    constexpr Iterator(Iterator &&) = default;
    constexpr Iterator & operator=(const Iterator &) = default;
    constexpr Iterator & operator=(Iterator &&) = default;

    // implementation details: data
private:
    index_type _current;      // the current value of the index
    shape_type _shape;        // the shape of the packing
    order_type _order;        // the index ordering determines the iteration order
};


// get the inline definitions
#define pyre_grid_Iterator_icc
#include "Iterator.icc"
#undef pyre_grid_Iterator_icc


#endif

// end of file
