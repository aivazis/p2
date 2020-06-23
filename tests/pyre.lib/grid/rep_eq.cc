// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// alias the rep
using rep_t = pyre::grid::rep_t<pyre::grid::size_t, 5>;


// make a {rep} that's filled with zeroes
int main(int argc, char * argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);
    pyre::journal::application("rep_eq");
    // make a channel
    pyre::journal::debug_t channel("pyre.grid.rep");

    // make a rep full of zeroes
    constexpr rep_t rep1 {};
    // and another
    constexpr auto rep2 = rep_t::zero();

    // verify they are equal
    static_assert (rep1 == rep2);

    // show me
    channel
        << "rep1: {" << rep1 << "}"
        << "rep2: {" << rep2 << "}"
        << pyre::journal::endl(__HERE__);

    // nothing to do
    return 0;
}


// end of file
