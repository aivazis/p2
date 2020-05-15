// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// external dependencies
#include "external.h"
// namespace setup
#include "forward.h"


// the module entry point
PYBIND11_MODULE(p2, m) {
    // the doc string
    m.doc() = "the journal extension module";

    // register the module api
    pyre::py::api(m);

    // get the timer bindings
    pyre::py::timers(m);
}


// end of file
