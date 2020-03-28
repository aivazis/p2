// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>


// alias
using chronicler_t = pyre::journal::chronicler_t;


// verify that the chronicler is accessible
int main() {
    // get the default device
    auto & device = chronicler_t::device();
    // verify that its the console
    assert (device.name() == "console");

    // all done
    return 0;
}


// end of file
