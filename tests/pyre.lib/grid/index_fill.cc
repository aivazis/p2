// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// type alias
using idx_t = pyre::grid::index_t<4>;


// compile time sanity check: make sure the header file is accessible
int main(int argc, char * argv[]) {
    // pick a value
    idx_t::axis_type u = 42;
    // make a const index
    const idx_t idx_1 { u };

    // verify the contents
    assert (idx_1[0] == u);
    assert (idx_1[1] == u);
    assert (idx_1[2] == u);
    assert (idx_1[3] == u);

    // again, at runtime
    idx_t::axis_type v = argc;
    // with another index
    const idx_t idx_2 { v };
    // verify the contents
    assert (idx_2[0] == v);
    assert (idx_2[1] == v);
    assert (idx_2[2] == v);
    assert (idx_2[3] == v);

    // all done
    return 0;
}


// end of file
