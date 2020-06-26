// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_forward_h)
#define pyre_grid_forward_h


// useful instantiations of STL entities
namespace pyre::grid {
    // the base class for the IndexIterator
    template <class packingT>
    using base_index_iterator =
        std::iterator<std::random_access_iterator_tag,        // category
                      typename packingT::index_type,          // iterators make indices
                      void,                                   // distance
                      const typename packingT::index_type *,  // pointer
                      const typename packingT::index_type &   // reference
                      >;
}

// set up the namespace
namespace pyre::grid {
    // thin adaptor over a compile time container
    template <class containerT> class Rep;
    // basic representation of our multi-dimensional entities
    template <class containerT> class Product;
    // shapes: the number of possible values of each index
    template <size_t N, template <typename, size_t> class containerT> class Shape;
    // indices
    template <size_t N, template <typename, size_t> class containerT> class Index;
    // the order in which index axes are packed in memory
    template <size_t N, template <typename, size_t> typename containerT> class Order;

    // support for the canonical packing strategies
    // an ordered index generator
    template <class packingT> class IndexIterator;
    // the packing strategy
    template <size_t N, template <typename, size_t> class containerT> class Canonical;
}


// operators on rep
namespace pyre::grid {
    // equality
    template <class containerT>
    constexpr auto
    operator== (const Rep<containerT> &, const Rep<containerT> &) -> bool;

    // stream injection
    template <class containerT>
    inline auto
    operator<< (ostream_reference, const Rep<containerT> &) -> ostream_reference;
}


// index iterator operators
namespace pyre::grid {
    // equality
    template <class packingT>
    constexpr auto
    operator==(const IndexIterator<packingT> &, const IndexIterator<packingT> &) -> bool;
    // and not
    template <class packingT>
    constexpr auto
    operator!=(const IndexIterator<packingT> &, const IndexIterator<packingT> &) -> bool;
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


#endif

// end of file
