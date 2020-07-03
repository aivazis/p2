// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <p2/memory.h>
// get the grid
#include <p2/grid.h>


// sanity check: make sure we can instantiate a grid
int main(int argc, char * argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);
    pyre::journal::application("grid_sanity");
    // make a channel
    pyre::journal::debug_t channel("pyre.grid");

    // we'll work with a 3d conventionally packed grid
    using pack_t = pyre::grid::canonical_t<3>;
    // of doubles on the heap
    using storage_t = pyre::memory::heap_t<double>;
    // putting it all together
    using grid_t = pyre::grid::grid_t<pack_t, storage_t>;

    // packing: 2x3x4
    pack_t packing { {2,3,4} };
    // whose capacity is
    auto cells = packing.capacity();
    // instantiate the grid
    grid_t grid { packing, std::make_shared<storage_t>(cells) };

    // make an index
    grid_t::index_type zero {};
    // set a value
    grid[zero] = 42;
    // show me the value
    channel
        << "grid[0,0,0] = " << grid[{0,0,0}]
        << pyre::journal::endl(__HERE__);

    // check
    assert(( grid[zero] == 42 ));

    // nothing to do
    return 0;
}


// end of file
