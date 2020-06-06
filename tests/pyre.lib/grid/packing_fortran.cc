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
    constexpr packing_t p = packing_t::fortran();

    static_assert (p[0] == 0);
    static_assert (p[1] == 1);
    static_assert (p[2] == 2);
    static_assert (p[3] == 3);

    // all done
    return 0;
}


// end of file
