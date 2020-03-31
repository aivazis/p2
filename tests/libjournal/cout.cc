// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>


// alias the type
using console_t = pyre::journal::cout_t;


// exercise the trivial device
int main() {
    // instantiate
    console_t console;
    // check its name
    assert (console.name() == "cout");

    // all done
    return 0;
}


// end of file
