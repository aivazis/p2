// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Packing_h)
#define pyre_grid_Packing_h


// generalization to multiple dimensions of the familiar row-major and column-major packing
// strategies. this is captured as a permutation in S_N that denotes the storage order of the
// indices.
template <pyre::grid::size_t N>
class pyre::grid::Packing : public Product<N, size_t> {
    // types
public:
    // alias for me
    using packing_type = Packing<N>;
    // alias for my base
    using product_type = Product<N, size_t>;
    // individual ranks
    using rank_type = typename product_type::rep_type::value_type;
    using rank_reference = rank_type &;
    using rank_const_reference = const rank_type &;

    // metamethods
public:
    // destructor: let the compiler do it
    ~Packing() = default;

    // a constructor that takes an initializer list
    template <typename... argT>
    constexpr explicit Packing(argT...);

    // static interface: factories
public:
    // c-like: last index varies first, in order right to left
    static constexpr auto rowMajor();
    // and it alias
    static constexpr auto c();

    // fortran-like: first index varies first, in order left to right
    static constexpr auto columnMajor();
    // and its alias
    static constexpr auto fortran();
};


// get the inline definitions
#define pyre_grid_Packing_icc
#include "Packing.icc"
#undef pyre_grid_Packing_icc


#endif

// end of file
