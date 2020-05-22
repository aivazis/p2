// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// access the memory package
#include <p2/memory.h>
// support
#include <cassert>


// type aliases
using cell_t = double;
using map_t = pyre::memory::map_t<cell_t>;


// create a new filemap
int main(int argc, char *argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);

    // the block size request
    std::size_t len = 1024;
    // create a new file-backed memory block of 1024 cells;
    map_t product("map.dat", len);

    // verify the capacity of the block
    assert(product.cells() == len);
    // check the size in bytes
    assert (product.bytes() == len * sizeof(cell_t));

    // make a cell
    cell_t value = 1;

    // go through the entire block
    for (auto & cell : product) {
        // verify it contains a zero
        assert (cell == 0);
        // and replace it with a new value
        cell = value;
    }

    // all done
    return 0;
}


// end of file
