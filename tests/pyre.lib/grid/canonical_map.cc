// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// type alias
using canonical_t = pyre::grid::canonical_t<3>;


// simple check that the map from index space to offsets is correct
int main(int argc, char * argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);
    pyre::journal::application("canonical_map");
    // make a channel
    pyre::journal::debug_t channel("pyre.grid.canonical");

    // pick a shape
    canonical_t::shape_type shape { 2,3,4 };
    // make a canonical packing strategy
    canonical_t packing { shape };

    // make an index
    canonical_t::index_type index { 1, 2, 3 };
    // get its offset
    auto offset = packing.offset(index);
    // map it back to an index
    auto image = packing.index(offset);

    // show me
    channel
        << "index: " << index << pyre::journal::newline
        << "offset: " << offset << pyre::journal::newline
        << "image: " << image << pyre::journal::endl(__HERE__);

    // verify that the {image} is our original index
    assert (image == index);

    // all done
    return 0;
}


// end of file
