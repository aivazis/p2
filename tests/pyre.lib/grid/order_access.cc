// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// type alias
using order_t = pyre::grid::order_t<4>;


// exercise operator[]
int main() {
    // make a constexpr index ordering
    constexpr order_t order_1 { 0, 1, 2, 3 };

    // verify the contents are available at compile time
    static_assert (order_1[0] == 0);
    static_assert (order_1[1] == 1);
    static_assert (order_1[2] == 2);
    static_assert (order_1[3] == 3);

    // make a writable one
    order_t order_2 { 0,0,0,0 };

    // set it
    order_2[0] = 0;
    order_2[1] = 1;
    order_2[2] = 2;
    order_2[3] = 3;

    // check it
    assert (order_2[0] == 0);
    assert (order_2[1] == 1);
    assert (order_2[2] == 2);
    assert (order_2[3] == 3);

    // all done
    return 0;
}


// end of file
