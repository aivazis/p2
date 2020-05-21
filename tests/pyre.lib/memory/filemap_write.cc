// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// access the memory package
#include <p2/memory.h>
// support
#include <cassert>


// type aliases
using filemap_t = pyre::memory::filemap_t;


// create a new filemap
int main(int argc, char *argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);

    // open an existing file-backed memory block for write
    filemap_t product("filemap.dat", true);

    // get the actual size
    auto bytes = product.size();
    // we expect a 4k block
    assert (bytes == 4*1024ul);

    // make a byte
    char value = 0x20;
    // access the block as an array of bytes
    auto data = static_cast<char *>(product.data());

    // go through the entire block
    for (std::size_t offset = 0; offset < bytes; ++offset) {
        // and fill it with our byte
        data[offset] = value;
    }

    // all done
    return 0;
}


// end of file
