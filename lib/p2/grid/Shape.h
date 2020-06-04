// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Shape_h)
#define pyre_grid_Shape_h


// the specification of the number of possible index values along each dimension
template <pyre::grid::size_t N>
class pyre::grid::Shape : public Product<N, size_t> {
    // types
public:
    // alias for me
    using shape_type = Shape<N>;
    // alias for my base
    using product_type = Product<N, size_t>;
    // individual axis values
    using axis_type = typename product_type::rep_type::value_type;
    using axis_reference = axis_type &;
    using axis_const_reference = const axis_type &;

    // metamethods
public:
    // destructor
    ~Shape() = default;

    // constructor; works with initializer lists
    template <typename... argT>
    constexpr explicit Shape(argT... args);
};


// get the inline definitions
#define pyre_grid_Shape_icc
#include "Shape.icc"
#undef pyre_grid_Shape_icc


#endif

// end of file
