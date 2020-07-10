// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// read a previously constructed memory mapped grid
int main(int argc, char * argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);
    pyre::journal::application("grid_mmap_get");
    // make a channel
    pyre::journal::debug_t channel("pyre.grid.mmap");

    // we'll work with a 3d conventionally packed grid
    using pack_t = pyre::grid::canonical_t<3>;
    // of doubles on the heap
    using storage_t = pyre::memory::constmap_t<double>;
    // putting it all together
    using grid_t = pyre::grid::grid_t<pack_t, storage_t>;

    // packing: 1024x1024x8
    pack_t packing { {1024,1024, 8} };
    // instantiate the grid
    grid_t grid { packing, "grid_mmap.data" };

    // show me the value at the origin
    channel
        << "grid[0,0,0] = " << grid[{0,0,0}]
        << pyre::journal::endl(__HERE__);

    // go through it in packing order
    for (const auto & idx : grid) {
        // and verify
        assert(( grid[idx] == grid.layout()[idx] ));
    }

    // nothing to do
    return 0;
}


// end of file
