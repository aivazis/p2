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


// exercise operator[]
int main() {
    // make a const index
    const shape_t shape_1 { 0,1,2,3 };

    // verify the contents
    assert (shape_1[0] == 0);
    assert (shape_1[1] == 1);
    assert (shape_1[2] == 2);
    assert (shape_1[3] == 3);

    // make a writable one
    shape_t shape_2 { 0,0,0,0 };

    // set it
    shape_2[0] = 0;
    shape_2[1] = 1;
    shape_2[2] = 2;
    shape_2[3] = 3;

    // check it
    assert (shape_2[0] == 0);
    assert (shape_2[1] == 1);
    assert (shape_2[2] == 2);
    assert (shape_2[3] == 3);

    // all done
    return 0;
}


// end of file
