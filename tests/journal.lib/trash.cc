// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// alias the type
using trash_t = pyre::journal::trash_t;


// exercise the trivial device
int main() {
    // instantiate
    trash_t trash;
    // check its name
    assert (trash.name() == "trash");

    // all done
    return 0;
}


// end of file
