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
    // register the exception types
    p2::libjournal::exceptions(m);
    // global state
    p2::libjournal::chronicler(m);
    // devices
    p2::libjournal::devices(m);
    // developer channels
    p2::libjournal::debug(m);
    p2::libjournal::firewall(m);
    // user facing channels
    p2::libjournal::info(m);
    p2::libjournal::warning(m);
}


// end of file
