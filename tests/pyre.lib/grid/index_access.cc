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


// exercise operator[]
int main() {
    // make a const index
    const idx_t idx_1 { 0,1,2,3 };

    // verify the contents
    assert (idx_1[0] == 0);
    assert (idx_1[1] == 1);
    assert (idx_1[2] == 2);
    assert (idx_1[3] == 3);

    // make a writable one
    idx_t idx_2 { 0,0,0,0 };

    // set it
    idx_2[0] = 0;
    idx_2[1] = 1;
    idx_2[2] = 2;
    idx_2[3] = 3;

    // check it
    assert (idx_2[0] == 0);
    assert (idx_2[1] == 1);
    assert (idx_2[2] == 2);
    assert (idx_2[3] == 3);

    // all done
    return 0;
}


// end of file
