// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_forward_h)
#define pyre_grid_forward_h


// set up the namespace
namespace pyre::grid {
    // thin adaptor over a compile time container
    template <typename T, size_t N, template <typename, size_t> class containerT>
    class Rep;

    // indices
    template <size_t N, template <typename, size_t> class containerT> class Index;

    // support for the canonical packing strategies
    // the order in which index axes are packed in memory
    template <size_t N, template <typename, size_t> typename containerT>
    class Order;

    // basic representation of our multi-dimensional entities
    template <size_t N, typename factorT> class Product;
    // shapes: the number of possible values of each index
    template <size_t N> class Shape;

    // support for the canonical packing strategies
    // an ordered index generator
    template <class packingT> class Iterator;
    // the packing strategy
    template <size_t N> class Canonical;
}


// operators on rep
namespace pyre::grid {
    // equality
    template <typename T, size_t N,
              template <typename, size_t> class containerT = std::array>
    inline auto
    operator== (const Rep<T,N,containerT> &, const Rep<T,N,containerT> &) -> bool;

    // stream injection
    template <typename T, size_t N,
              template <typename, size_t> class containerT = std::array>
    inline auto
    operator<< (ostream_reference, const Rep<T,N,containerT> &) -> ostream_reference;
}


// index algebra
namespace pyre::grid {
    // addition
    template <size_t N,
              template <typename, size_t> class containerT>
    constexpr auto
    operator+ (const Index<N, containerT> & i1, const Index<N, containerT> & i2)
        -> Index<N, containerT>;

    // subtraction
    template <size_t N,
              template <typename, size_t> class containerT>
    constexpr auto
    operator- (const Index<N, containerT> & i1, const Index<N, containerT> & i2)
        -> Index<N, containerT>;
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
}


#endif

// end of file
