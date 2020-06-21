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
    // pick the index origin
    canonical_t::index_type origin { -1, -1, -1 };
    // make a canonical packing strategy
    canonical_t packing { shape, origin };

    // check the nudge
    assert (packing.nudge() == -17);

    // all done
    return 0;
}


// end of file
