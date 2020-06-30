// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_forward_h)
#define pyre_grid_forward_h


// useful instantiations of STL entities
namespace pyre::grid {
    // the base class for {OrderIterator}
    template <class productT, bool isConst>
    using base_order_iterator =
        std::iterator<std::forward_iterator_tag,
                     typename productT::value_type,             // points to index ranks
                     typename productT::difference_type,        // distance among entries
                     std::conditional<isConst,
                                      typename productT::const_pointer,
                                      typename productT::pointer>,
                     std::conditional<isConst,
                                      typename productT::const_reference,
                                      typename productT::reference>
                     >;

    // the base class for {IndexIterator}
    template <class packingT>
    using base_index_iterator =
        std::iterator<std::forward_iterator_tag,              // category
                      typename packingT::index_type,          // points to index instances
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
    template <class containerT> class Shape;
    // indices
    template <class containerT> class Index;
    // index rank ordering, e.g. the order in which index axes are packed in memory
    template <class containerT> class Order;
    // support for visiting ranks in a specific order
    template <class productT, class orderIteratorT, bool isConst> class OrderIterator;

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
    operator==(const Rep<containerT> &, const Rep<containerT> &) -> bool;

    // stream injection
    template <class containerT>
    inline auto
    operator<<(ostream_reference, const Rep<containerT> &) -> ostream_reference;
}


// order iterator operators
namespace pyre::grid {
    // equality
    template <class productT, class orderIteratorT, bool isConst>
    constexpr auto
    operator==(const OrderIterator<productT, orderIteratorT, isConst> &,
               const OrderIterator<productT, orderIteratorT, isConst> &) -> bool;
    // and not
    template <class productT, class orderIteratorT, bool isConst>
    constexpr auto
    operator!=(const OrderIterator<productT, orderIteratorT, isConst> &,
               const OrderIterator<productT, orderIteratorT, isConst> &) -> bool;
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
    template <class containerT>
    constexpr auto
    operator+ (const Index<containerT> & i1, const Index<containerT> & i2)
        -> Index<containerT>;

    // subtraction
    template <class containerT>
    constexpr auto
    operator- (const Index<containerT> & i1, const Index<containerT> & i2)
        -> Index<containerT>;
}


#endif

// end of file
