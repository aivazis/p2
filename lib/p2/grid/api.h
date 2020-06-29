// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_api_h)
#define pyre_grid_api_h


// low level entities; you should probably stay away from them
namespace pyre::grid
{
    // this wrapper over a {std::array}-like container
    // thin adaptor over a compile time container
    template <typename T, size_t N, template <typename, size_t> class containerT = std::array>
    using rep_t = Rep<containerT<T,N>>;

    // support for the multidimensional objects in this package
    template <size_t N, typename T = size_t,
              template <typename, size_t> class containerT = std::array>
    using product_t = Product<containerT<T,N>>;

    // the number of possible values of each axis
    template <size_t N, template <typename, size_t> class containerT = std::array>
    using shape_t = Shape<N, containerT>;

    // indices
    template <size_t N, typename T = int,
              template <typename, size_t> class containerT = std::array>
    using index_t = Index<containerT<T,N>>;

    // the order in which indices are packed in memory
    template <size_t N, template <typename, size_t> class containerT = std::array>
    using order_t = Order<N, containerT>;

    // in order product rank traversal
    template <class productT, class orderT, bool isConst = true>
    using order_iterator_t = OrderIterator<productT, orderT, isConst>;

    // ordered index generator
    template <class packingT>
    using index_iterator_t = IndexIterator<packingT>;
    // the canonical packing strategy
    template <size_t N, template <typename, size_t> class containerT = std::array>
    using canonical_t = Canonical<N, containerT>;
}


#endif

// end of file
