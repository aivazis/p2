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
    cell_t cell = 1;
    // access the block as an array of bytes
    auto data = product.data();

    // go through the entire block
    for (std::size_t offset = 0; offset < product.cells(); ++offset) {
        // verify it contains a zero
        assert (data[offset] == 0);
        // and replace it with a new value
        data[offset] = cell;
    }

    // all done
    return 0;
}


// end of file
