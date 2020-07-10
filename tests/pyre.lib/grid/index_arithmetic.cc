// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// type alias
using index_t = pyre::grid::index_t<2>;


// shape arithmetic
int main(int argc, char * argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);
    pyre::journal::application("index_arithmetic");
    // make a channel
    pyre::journal::debug_t channel("pyre.grid.index");

    // make a couple of shapes
    constexpr index_t ref { 128, 128 };
    constexpr index_t sec { 192, 192 };

    // make a shape out a combination of these
    index_t cor = sec - ref + index_t::one();

    // show me
    channel
        << "ref: " << ref << pyre::journal::newline
        << "sec: " << sec << pyre::journal::newline
        << "cor: " << cor << pyre::journal::endl(__HERE__);


    // verify
    for (size_t axis = 0; axis < index_t::rank(); ++axis) {
        assert(( cor[axis] == sec[axis] - ref[axis] + 1 ));
    }

    // all done
    return 0;
}


// end of file