// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_forward_h)
#define pyre_grid_forward_h


// set up the namespace
namespace pyre::grid {
    // basic representation of our multi-dimensional entities
    template <size_t N, typename factorT> class Product;
    // indices
    template <size_t N> class Index;
    // shapes: the number of possible values of each index
    template <size_t N> class Shape;

    // memory packing strategies
    // the order in which index axes are packed in memory
    template <size_t N> class Order;
    // the packing strategy
    template <size_t N> class Canonical;
}


// operators
namespace pyre::grid {
    // boolean operators for {Product} descendants
    // equality
    template <size_t N, typename factorT>
    constexpr bool
    operator==(const Product<N, factorT> &, const Product<N, factorT> &);
    // and not
    template <size_t N, typename factorT>
    constexpr bool
    operator!=(const Product<N, factorT> &, const Product<N, factorT> &);

    // stream injection for {Product} descendants
    template <size_t N, typename factorT>
    auto
    operator<< (ostream_reference, const Product<N, factorT> & index) -> ostream_reference;

    // index algebra
    template <size_t N>
    constexpr auto
    operator+ (const Index<N> & i1, const Index<N> & i2) -> Index<N>;

    template <size_t N>
    constexpr auto
    operator- (const Index<N> & i1, const Index<N> & i2) -> Index<N>;
}


#endif

// end of file
