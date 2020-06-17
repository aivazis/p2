// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// type alias
using shape_t = pyre::grid::shape_t<4>;


// sanity check
int main() {
    // make a shape
    shape_t s { 2, 2, 2, 2 };

    // verify that the index dimensionality is reported correctly through the type
    static_assert (shape_t::dim() == 4);
    // verify that the index dimensionality is reported correctly through an instance
    static_assert (s.dim() == 4);

    // verify that a shape is equal to itself
    assert (s == s);

    // make another
    shape_t z { 0, 0, 0, 0 };
    // that's not equal to {s}
    assert (s != z);

    // all done
    return 0;
}


// end of file
