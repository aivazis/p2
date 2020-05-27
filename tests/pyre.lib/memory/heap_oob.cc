// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the memory
#include <p2/memory.h>
// support
#include <cassert>


// type alias
using heap_t = pyre::memory::heap_t<double, true>;


// verify that we can construct and use heap blocks
int main(int argc, char * argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);
    pyre::journal::application("heap_oob");

    // silence the firewall
    pyre::journal::firewall_t::quiet();

    // the number of cells
    std::size_t cells = 1024ul;
    // make a block on the heap
    heap_t product(cells);

    // gingerly
    try {
        // make an out-of-bounds access
        product[product.cells()];
        // unreachable
        throw std::logic_error("unreachable");
    // catch the firewall
    } catch (const pyre::journal::firewall_t::exception_type &) {
        // all good
    }

    // all done
    return 0;
}


// end of file