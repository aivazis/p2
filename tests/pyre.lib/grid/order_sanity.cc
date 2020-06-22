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


// sanity check
int main() {
    // make an index ordering
    order_t shuffle { 0, 1, 2, 3 };

    // verify that the dimensionality is reported correctly through the type
    static_assert (order_t::rank() == 4);
    // verify that the dimensionality is reported correctly through an instance
    static_assert (shuffle.rank() == 4);

    // make a column major ordering
    order_t fortran = order_t::fortran();
    // check that it's equal to {shuffle}
    assert (shuffle == fortran);

    // make a column major ordering
    order_t c = order_t::c();
    // check that it's different from {shuffle}
    assert (!(shuffle == c));

    // all done
    return 0;
}


// end of file
