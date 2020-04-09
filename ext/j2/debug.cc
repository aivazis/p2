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
debug(py::module & m) {

    // debug channels
    py::class_<debug_t>(m, "Debug")
        // the constructor
        .def(py::init<const string_t &>(), "name"_a)
        // accessors
        .def("name", &debug_t::name)
        .def("state", (bool (debug_t::*)() const) &debug_t::state)
        .def("device", (debug_t::device_pointer (debug_t::*)() const) &debug_t::device)
        // static interface
        .def_static("defaultState", &debug_t::defaultState)
        .def_static("defaultDevice", (debug_t::device_pointer (*)()) &debug_t::defaultDevice)
        // done
        ;

    // all done
    return;
}


// end of file
