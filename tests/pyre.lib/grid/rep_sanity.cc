// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the grid
#include <p2/grid.h>


// alias the rep
template <pyre::grid::size_t N>
using rep_t = pyre::grid::rep_t<pyre::grid::size_t, N>;


// exercise the basic {rep_t} interface
int main(int argc, char * argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);
    pyre::journal::application("rep_sanity");
    // make a channel
    pyre::journal::debug_t channel("pyre.grid.rep");

    // make a rep
    constexpr rep_t<4> rep { 0, 1, 2, 3 };

    // check the dimension
    static_assert (rep.rank() == 4);
    // and the contents
    static_assert (rep[0] == 0);
    static_assert (rep[1] == 1);
    static_assert (rep[2] == 2);
    static_assert (rep[3] == 3);

    // show me
    channel
        << "rep: {" << rep << "}"
        << pyre::journal::endl(__HERE__);

    // all done
    return 0;
}


// end of file
