// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// type aliases
using ansi_t = pyre::journal::ansi_t;


// exercise the trivial device
int main(int argc, char *argv[]) {

    // the user hands his expectation
    bool expectation = argc > 1 ? std::atoi(argv[1]) : true;
    // ask the wrapper whether the underlying terminal type is ANSI compatible
    auto observation = ansi_t::compatible();

    // verify that expectation and observation match
    assert (expectation == observation);

    // all done
    return 0;
}


// end of file
