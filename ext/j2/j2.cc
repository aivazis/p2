// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// external dependencies
#include "external.h"
// namespace setup
#include "forward.h"


// the module entry point
PYBIND11_MODULE(j2, m) {
    // the doc string
    m.doc() = "the journal extension module";

    // bind the opaque types
    p2::libjournal::opaque(m);
    // global state
    p2::libjournal::chronicler(m);
    // devices
    p2::libjournal::devices(m);
    // channels
    p2::libjournal::debug(m);
}


// end of file
