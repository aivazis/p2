// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>

// type alias
using product_t = pyre::grid::product_t<4>;


// exercise iterating over products
int main()
{
    // make one
    product_t p {0, 1, 2, 3};

    // fill
    for (auto & f : p) {
        // with a specific value
        f = 42;
    }

    // check
    for (auto f : p) {
        // that we get what we expect
        assert(f == 42);
    }

    // all done
    return 0;
}


// end of file
