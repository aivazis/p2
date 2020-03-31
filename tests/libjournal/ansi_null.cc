// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>


// type aliases
using ansi_t = pyre::journal::ansi_t;


#include <iostream>
// exercise the trivial device
int main(int argc, char *argv[]) {
    // verify that the null color table support all possible requests
    auto & strange = ansi_t::null["a-very-unlikely-color-name"];
    // and that the color sequences it returns are empty strings
    assert (strange.empty());

    // all done
    return 0;
}


// end of file
