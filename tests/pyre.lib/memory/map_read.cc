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
using map_t = pyre::memory::map_t<cell_t, true>;


// create a map over an existing product in read-only mode
int main(int argc, char *argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);

    // open an existing file-backed memory block
    map_t product("map.dat");

    // check the capacity of the block
    assert (product.cells() == 1024);
    // and the size in bytes
    assert (product.bytes() == product.cells() * sizeof(map_t::cell_type));

    // go through the entire block
    for (auto cell : product) {
        // verify the contents
        assert (cell == 2);
    }

    // all done
    return 0;
}


// end of file