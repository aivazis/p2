// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// alias the rep
using rep_t = pyre::grid::rep_t<pyre::grid::size_t, 4>;


// exercise the iteration protocol support
int main(int argc, char * argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);
    pyre::journal::application("rep_iteration");
    // make a channel
    pyre::journal::debug_t channel("pyre.grid.rep");

    // make a rep
    constexpr rep_t rep = rep_t::zero();
    // go through its contents
    for (auto r = rep.rbegin(); r != rep.rend(); ++r) {
        // and make sure it is zero
        assert(( *r == 0 ));
    }

    // show me
    channel
        << "rep: {" << rep << "}"
        << pyre::journal::endl(__HERE__);

    // nothing to do
    return 0;
}


// end of file
