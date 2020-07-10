// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <p2/memory.h>
// get the grid
#include <p2/grid.h>


// a non-trivial example: a sum area table; the calculations are done with raw indices
int main(int argc, char * argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);
    pyre::journal::application("grid_sat_slice");
    // make a channel
    pyre::journal::debug_t channel("pyre.grid.heap");

    // we'll work with a 3d conventionally packed grid
    using pack_t = pyre::grid::canonical_t<2>;
    // of doubles on the heap
    using storage_t = pyre::memory::heap_t<double>;
    // putting it all together
    using grid_t = pyre::grid::grid_t<pack_t, storage_t>;

    // pick the shape
    // constexpr pack_t::shape_type shape { 1024, 1024 };
    constexpr pack_t::shape_type shape { 2, 3 };
    // packing: 1024x1024
    pack_t packing { shape };
    // instantiate the grid
    grid_t grid { packing, packing.capacity() };
    // pick a value
    double value = 1;
    // fill it
    for (const auto & idx : grid) {
        // with our chosen value
        grid[idx] = value;
    }

    // make the sum area table
    grid_t sat { packing, packing.capacity() };

    // fill the top corner
    sat[{0,0}] = grid[{0,0}];
    // show me
    channel << "-- origin" << pyre::journal::newline;
    channel << "sat[0, 0] <- " << sat[{0,0}] << pyre::journal::newline;

    channel << "-- top row" << pyre::journal::newline;
    // the top row minus the origin
    auto topRow = grid.box( {0,1}, {1, shape[1]-1} );
    // fill the top row
    for (const auto & idx : topRow) {
        // place the value
        sat[idx] = grid[idx] + sat[idx - grid_t::index_type({0,1})];
        // show me
        channel << "sat[" << idx << "] <- " << sat[idx] << pyre::journal::newline;
    }

    channel << "-- left column" << pyre::journal::newline;
    // the left column minus the origin
    auto leftCol = grid.box( {1, 0}, {shape[0]-1, 1} );
    // fill the left column
    for (const auto & idx : leftCol) {
        // place the value
        sat[idx] = grid[idx] + sat[idx - grid_t::index_type({1,0})];
        // show me
        channel << "sat[" << idx << "] <- " << sat[idx] << pyre::journal::newline;
    }

    channel << "-- body" << pyre::journal::newline;
    // the rest of the table
    auto body = grid.box( {1,1}, {shape[0]-1, shape[1]-1} );
    // fill it
    for (const auto & idx : body) {
        // compute
        sat[idx] =
            grid[idx]
            + sat[idx - grid_t::index_type({1,0})]
            + sat[idx - grid_t::index_type({0,1})]
            - sat[idx - grid_t::index_type({1,1})];
        // show me
        channel << "sat[" << idx << "] <- " << sat[idx] << pyre::journal::newline;
    }
    channel << "--" << pyre::journal::newline;
    // flush
    channel << pyre::journal::endl;

    // verify
    for (const auto & idx : sat) {
        // the expected value
        double expected = (idx[0]+1) * (idx[1]+1) * value;
        // show me
        channel
            << "sat[" << idx << "] = " << sat[idx] << ", expected: " << expected
            << pyre::journal::newline;
        // compare
        // assert(( sat[idx] == expected ));
    }
    // flush
    channel << pyre::journal::endl;

    // nothing to do
    return 0;
}


// end of file