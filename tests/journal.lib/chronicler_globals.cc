// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// alias
using chronicler_t = pyre::journal::chronicler_t;


// verify that the chronicler is accessible
int main() {
    // get the global metadata
    auto & metadata = chronicler_t::globals();

    // tag
    chronicler_t::key_type key("application");
    chronicler_t::value_type value("chronicler");
    // insert it
    metadata[key] = value;

    // look for it
    auto direct = chronicler_t::globals().find(key);
    // verify its there
    assert (direct != chronicler_t::globals().end());
    // and it is the right one
    assert (direct->first == key);
    assert (direct->second == value);

    // all this should be true through our original access reference
    auto ref = metadata.find(key);
    // verify its there
    assert (ref != metadata.end());
    // and it is the right one
    assert (ref->first == key);
    assert (ref->second == value);

    // all done
    return 0;
}


// end of file