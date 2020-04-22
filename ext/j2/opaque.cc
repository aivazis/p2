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
opaque(py::module & m) {
    // the channel ocontents
    py::bind_vector<pyre::journal::page_t>(m, "Page");

    // the channel metadata type
    py::bind_map<pyre::journal::metadata_t>(m, "Metadata");

    // all done
    return;
}


// end of file
