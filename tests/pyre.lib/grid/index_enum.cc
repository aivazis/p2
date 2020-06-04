// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the grid
#include <p2/grid.h>


// type alias
using idx_t = pyre::grid::index_t<2>;

// color choices
enum class color : int { red, green, blue };
// polarization choices
enum class pol : int { hh, hv, vh, vv };


// check the enums can be used as indices
int main() {
    // make an index
    idx_t idx { pol::hh, color::red };
    // nothing to do
    return 0;
}


// end of file
