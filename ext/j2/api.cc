// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// externals
#include "external.h"
// namespace setup
#include "forward.h"


// add bindings to the inventory
void
p2::libjournal::
api(py::module & m) {
    // easy access to the manager of the global state
    m.attr("chronicler") = m.attr("Chronicler");

    // registration of the application name
    m.def("application",
          // the implementation
          &pyre::journal::application, "name"_a,
          // the docstring
          "register the application {name}"
          );

    // all done
    return;
}


// end of file
