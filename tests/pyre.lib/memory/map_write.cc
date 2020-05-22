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

    // open an existing file-backed memory block for write
    map_t product("map.dat", true);

    // check the capacity of the block
    assert (product.cells() == 1024);
    // and the size in bytes
    assert (product.bytes() == product.cells() * sizeof(map_t::cell_type));

    // access the block as an array of bytes
    auto data = product.data();

    // go through the entire block
    for (std::size_t offset = 0; offset < product.cells(); ++offset) {
        // verify the contents
        assert (data[offset] == 1);
        // and change it
        data[offset] *= 2;
    }

    // all done
    return 0;
}


// end of file
