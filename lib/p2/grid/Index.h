// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Index_h)
#define pyre_grid_Index_h


// storage for a multidimensional index
// resist the temptation to use unsigned types as the fundamental representation type; they
// complicate index arithmetic unnecessarily

// basic index type
template <pyre::grid::size_t N, template <typename, size_t> class containerT>
class pyre::grid::Index : public Product<containerT<int, N>> {
    // types
public:
    // alias for me
    using index_type = Index<N, containerT>;
    // alias for my base
    using rep_type = Product<containerT<int, N>>;
    // individual axis values
    using axis_type = typename rep_type::value_type;
    using axis_reference = axis_type &;
    using axis_const_reference = const axis_type &;

    // metamethods
public:
    // constructor that fills an index with a given {value}
    constexpr explicit Index(axis_type);

    // constructor; a variadic template to enable initializer lists
    template <typename... argT>
    constexpr explicit Index(argT...);

    // static interface: factories
public:
    static constexpr auto zero() -> index_type;

    // default metamethods
public:
    // destructor
    ~Index() = default;
    // constructors
    Index(const Index &) = default;
    Index(Index &&) = default;
    Index & operator=(const Index &) = default;
    Index & operator=(Index &&) = default;
};


// get the inline definitions
#define pyre_grid_Index_icc
#include "Index.icc"
#undef pyre_grid_Index_icc


#endif

// end of file
