// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Shape_h)
#define pyre_grid_Shape_h


// the specification of the number of possible index values along each dimension
// this class stores the {s_i} in
//
//     Z_s_0 x ... x Z_s_{n-1}
//
template <pyre::grid::size_t N, template <typename, size_t> class containerT>
class pyre::grid::Shape : public Rep<containerT<size_t, N>> {
    // types
public:
    // alias for me
    using shape_type = Shape<N, containerT>;
    // alias for my base
    using rep_type = Rep<containerT<size_t, N>>;
    // the sizes of things
    using size_type = typename rep_type::size_type;
    // individual axis values
    using axis_type = typename rep_type::value_type;
    using axis_reference = axis_type &;
    using axis_const_reference = const axis_type &;

    // metamethods
public:
    // constructor; works with initializer lists
    template <typename... argT>
    constexpr explicit Shape(argT... args);

    // interface
public:
    // the total number of addressable values
    constexpr auto capacity() const -> size_type;

    // default metamethods
public:
    // destructor
    ~Shape() = default;
    // constructors
    Shape(const Shape &) = default;
    Shape(Shape &&) = default;
    Shape & operator=(const Shape &) = default;
    Shape & operator=(Shape &&) = default;
};


// get the inline definitions
#define pyre_grid_Shape_icc
#include "Shape.icc"
#undef pyre_grid_Shape_icc


#endif

// end of file
