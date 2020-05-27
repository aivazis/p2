// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// type alias
using idx_t = pyre::grid::index_t<4, true>;


// compile time sanity check: make sure the header file is accessible
int main(int argc, char * argv[]) {
    // make a const index
    const idx_t idx_1 { 42 };

    // verify the contents
    assert (idx_1[0] == 42);
    assert (idx_1[1] == 42);
    assert (idx_1[2] == 42);
    assert (idx_1[3] == 42);

    // again, at runtime
    idx_t::idx_type v = argc;
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
