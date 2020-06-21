// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
#include <iostream>
// get the grid
#include <p2/grid.h>


// type alias
using canonical_t = pyre::grid::canonical_t<3>;


// simple check that the map to and from index space is correct in the presence of a
// non-trivial origin
int main() {
    // pick a shape
    canonical_t::shape_type shape { 3, 5, 7 };
    // the indices range from (-1, -2)  to (1, 2)
    canonical_t::index_type origin { -1, 0, 0 };
    // and the cells are in c mode (the default)
    auto order = canonical_t::order_type::c();
    // assemble a canonical packing strategy
    canonical_t packing { shape, origin, order };

    // verify that the offset of the {origin} is zero
    assert (packing.offset(origin) == 0);
    // verify that the offset of {0,0,0} is equal to the nudge
    assert (packing.offset({0,0,0}) == -packing.nudge());

    // make an index
    canonical_t::index_type index { 1, 2, 3 };
    // get its offset
    auto offset = packing.offset(index);
    // map it back to an index
    auto image = packing.index(offset);

    // show me
    std::cout
        << "shape: " << packing.shape() << std::endl
        << "origin: " << packing.origin() << std::endl
        << "order: " << packing.order() << std::endl
        << "strides: " << packing.strides() << std::endl
        << "nudge: " << packing.nudge() << std::endl
        << "index: " << index << std::endl
        << "offset: " << offset << std::endl
        << "image: " << image << std::endl;

    // verify that the {image} is our original index
    assert (image == index);
    //

    // all done
    return 0;
}


// end of file
