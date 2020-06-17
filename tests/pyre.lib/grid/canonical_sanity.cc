// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// type alias
using canonical_t = pyre::grid::canonical_t<3>;


// compile time sanity check: make sure the header file is accessible
int main() {
    // pick a shape
    canonical_t::shape_type shape { 2,3,4 };
    // make a canonical packing strategy
    canonical_t packing { shape };

    // verify we understand the default constructor
    assert (packing.shape() == shape);
    assert (packing.order() == canonical_t::order_type::c());
    assert (packing.origin() == canonical_t::index_type::zero());
    assert (packing.nudge() == 0);

    // all done
    return 0;
}


// end of file
