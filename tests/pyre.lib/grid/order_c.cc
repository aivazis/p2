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
    // make a constexpr row major index ordering
    constexpr order_t p = order_t::c();

    // verify the contents are accessible at compile time
    static_assert (p[0] == 3);
    static_assert (p[1] == 2);
    static_assert (p[2] == 1);
    static_assert (p[3] == 0);

    // all done
    return 0;
}


// end of file
