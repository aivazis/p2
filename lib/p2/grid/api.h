// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_api_h)
#define pyre_grid_api_h

// user facing types
namespace pyre::grid
{
}

// low level entities; you should probably stay away from them
namespace pyre::grid
{
    // support for the multidimensional objects in this package
    template <size_t N, typename factorT = size_t>
    using product_t = Product<N, factorT>;

    // indices
    template <size_t N>
    using index_t = Index<N>;
}

#endif

// end of file
