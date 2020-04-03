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
    // get the global metadata map
    chronicler_t::metadata_type & globals = chronicler_t::globals();

    // there should be only one setting for now
    assert (globals.size() == 1);
    // verify the known contents
    assert (globals.at("application") == "journal");

    // get the default device
    auto device_ptr = chronicler_t::device();
    // by default, it is the console; verify that it is not an empty pointer
    assert(device_ptr);
    // and that it's the console
    assert ((*device_ptr).name() == "cout");

    // all done
    return 0;
}


// end of file
