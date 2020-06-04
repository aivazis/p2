// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the grid
#include <p2/grid.h>


// type alias
using shape_t = pyre::grid::shape_t<4>;


// sanity check: make sure the header file is accessible and that we can access
// the dimension of a shape
int main() {
    // make a shape
    shape_t s { 0,0,0,0 };

    // verify that the index dimensionality is reported correctly through the type
    static_assert (shape_t::dim() == 4);
    // verify that the index dimensionality is reported correctly through an instance
    static_assert (s.dim() == 4);

    // all done
    return 0;
}


// end of file
