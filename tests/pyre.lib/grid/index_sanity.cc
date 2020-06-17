// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// type alias
using index_t = pyre::grid::index_t<4>;


// sanity check
int main() {
    // make an index
    index_t idx { 0,0,0,0 };

    // verify that the index dimensionality is reported correctly through the type
    static_assert (index_t::dim() == 4);
    // verify that the index dimensionality is reported correctly through an instance
    static_assert (idx.dim() == 4);

    // make a zero index using the static factory
    index_t z = index_t::zero();
    // verify it's the same as {idx}
    assert (idx == z);

    // make an index using the filling constructor
    index_t one(1);
    // verify it's not the same as {idx}
    assert (idx != one);

    // all done
    return 0;
}


// end of file
