// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// type alias
using idx_t = pyre::grid::index_t<2, true>;


// compile time sanity check: make sure the header file is accessible
int main(int argc, char * argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);
    pyre::journal::application("index_oob");

    // silence the firewall
    pyre::journal::firewall_t::quiet();

    // make a const index
    const idx_t cidx { 0,1 };

    // carefully
    try {
        // make an out-of-bounds access
        cidx[cidx.dim()];
        // we shouldn't get here
        throw std::logic_error("unreachable");
   // catch it
    } catch (const pyre::journal::firewall_t::exception_type &) {
        // all good
    }

    // make a non-const index
    idx_t idx { 0,1 };

    // carefully
    try {
        // make an out-of-bounds access
        idx[idx.dim()] = 2;
        // we shouldn't get here
        throw std::logic_error("unreachable");
   // catch it
    } catch (const pyre::journal::firewall_t::exception_type &) {
        // all good
    }

    // all done
    return 0;
}


// end of file
