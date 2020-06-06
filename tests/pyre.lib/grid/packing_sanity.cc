// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the grid
#include <p2/grid.h>


// type alias
using packing_t = pyre::grid::packing_t<4>;


// compile time sanity check: make sure the header file is accessible
int main() {
    // make an index
    packing_t p { 0, 1, 2, 3 };

    // verify that the index dimensionality is reported correctly through the type
    static_assert (packing_t::dim() == 4);
    // verify that the index dimensionality is reported correctly through an instance
    static_assert (p.dim() == 4);

    // all done
    return 0;
}


// end of file
