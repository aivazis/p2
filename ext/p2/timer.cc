// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// externals
#include "external.h"
// namespace setup
#include "forward.h"


// type alias
using timer_t = pyre::timers::timer_t;


// add bindings timers
void
pyre::py::
timers(py::module & m) {

    // the timer interface
    py::class_<timer_t>(m, "Timer")
        // the constructor
        .def(py::init<const timer_t::name_type &>(), "name"_a)

        // accessors
        // the name; read-only property
        .def_property_readonly("name",
                               // the implementation
                               &timer_t::name,
                               // the docstring
                               "my name")

        // done
        ;

    // all done
    return;
}


// end of file
