// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// disable the debug channels
#define NDEBUG
#undef PYRE_CORE
// get the journal
#include <j2/journal.h>

// re-enable debugging support so we have assert
#undef NDEBUG
// support
#include <cassert>


// verify that when NDEBUG is on, {debug_t} becomes {null_t}
int main() {
    // verify that {debug_t} is a {null_t}
    assert ((std::is_same<pyre::journal::debug_t, pyre::journal::null_t>::value));

    // all done
    return 0;
}


// end of file
