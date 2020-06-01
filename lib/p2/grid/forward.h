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
    template <size_t N, bool checkBounds> class Index;
};


#endif

// end of file
