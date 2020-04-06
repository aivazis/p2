// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

#include <iostream>
// get the journal
#include <j2/journal.h>
// support
#include <cassert>


// aliases
using string_t = pyre::journal::string_t;
using nameset_t = pyre::journal::nameset_t;
using chronicler_t = pyre::journal::chronicler_t;


// verify that the verbosity level set in the environment matches what the test harness gave me
// on the command line
int main() {
    // form the test case
    string_t input = ",,,foo,bar,,baz,,bab,,,";
    // the correct answer
    nameset_t expected { "bab", "foo", "bar", "baz" };
    // ask the {chronicler} to parse it
    auto names = chronicler_t::nameset(input);
    // verify
    assert (names == expected);

    // all done
    return 0;
}


// end of file
