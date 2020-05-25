// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the grid
#include <p2/grid.h>


// type alias
using idx_t = pyre::grid::index_t<4, true>;


// compile time sanity check: make sure the header file is accessible
int main() {
    // make an index
    idx_t t { 0,0,0,0 };

    // verify that the index dimensionality is reported correctly through the type
    static_assert (idx_t::dim() == 4);
    // verify that the index dimensionality is reported correctly through an instance
    static_assert (t.dim() == 4);

    // all done
    return 0;
}


// end of file
