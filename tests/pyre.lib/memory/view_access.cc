// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the memory
#include <p2/memory.h>
// support
#include <cassert>


// type alias
using view_t = pyre::memory::view_t<double, true>;


// compile time sanity check: make sure the header file is accessible
int main() {
    // the number of cells
    std::size_t cells = 1024ul;
    // allocate a memory block
    double * block = new double[cells];

    // convert it into a view
    view_t view(block, cells);

    // verify we can iterate and write
    for (auto & cell : view) {
        // to zero
        cell = 0;
    }

    // verify we can iterate and read
    for (auto cell : view) {
        // check that we have what we expect
        assert (cell == 0);
    }

    // exercise operator []
    // write
    view[cells/2] = 1;
    // and read
    assert (view[cells/2] == 1);

    // clean up
    delete [] block;

    // all done
    return 0;
}


// end of file
