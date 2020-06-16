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
};


#endif

// end of file
