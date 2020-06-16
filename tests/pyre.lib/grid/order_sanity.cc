// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the grid
#include <p2/grid.h>


// type alias
using order_t = pyre::grid::order_t<4>;


// compile time sanity check: make sure the header file is accessible
int main() {
    // make an index ordering
    order_t shuffle { 0, 1, 2, 3 };

    // verify that the dimensionality is reported correctly through the type
    static_assert (order_t::dim() == 4);
    // verify that the dimensionality is reported correctly through an instance
    static_assert (shuffle.dim() == 4);

    // all done
    return 0;
}


// end of file
