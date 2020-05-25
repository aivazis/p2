// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_api_h)
#define pyre_grid_api_h


// user facing types
namespace pyre::grid {

}


// low level entities; you should probably stay away from them
namespace pyre::grid {
    // indices
    template <size_t N, bool checkBounds=false>
    using index_t = Index<N, checkBounds>;
}


#endif

// end of file
