// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// type alias
using packing_t = pyre::grid::packing_t<4>;


// exercise operator[]
int main() {
    // make a const index
    const packing_t packing_1 { 0, 1, 2, 3 };

    // verify the contents
    assert (packing_1[0] == 0);
    assert (packing_1[1] == 1);
    assert (packing_1[2] == 2);
    assert (packing_1[3] == 3);

    // make a writable one
    packing_t packing_2 { 0,0,0,0 };

    // set it
    packing_2[0] = 0;
    packing_2[1] = 1;
    packing_2[2] = 2;
    packing_2[3] = 3;

    // check it
    assert (packing_2[0] == 0);
    assert (packing_2[1] == 1);
    assert (packing_2[2] == 2);
    assert (packing_2[3] == 3);

    // all done
    return 0;
}


// end of file
