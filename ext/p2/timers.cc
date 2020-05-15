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

        // the registry; read-only static property
        .def_property_readonly_static("registry",
                                      // the implementation
                                      [](py::object) -> timer_t::registry_reference {
                                          return timer_t::registry();
                                      },
                                      // the docstring
                                      "the timer registry")
        // interface
        // start
        .def("start",
             // implementation
             &timer_t::start,
             // docstring
             "start the timer")
        // stop
        .def("stop",
             // implementation
             &timer_t::stop,
             // doctstring
             "stop the timer")
        // reset
        .def("reset",
             // implementation
             &timer_t::reset,
             // docstring
             "reset the timer")
        // read
        .def("read",
             // implementation
             &timer_t::read,
             // docstring
             "get the accumulated time")
        // as a string, in seconds
        .def("sec",
             // implementation
             &timer_t::sec,
             // docstring
             "render the accumulated time in seconds")
        // as a string, in milliseconds
        .def("ms",
             // implementation
             &timer_t::ms,
             // docstring
             "render the accumulated time in milliseconds")
        // as a string, in microseconds
        .def("us",
             // implementation
             &timer_t::us,
             // docstring
             "render the accumulated time in microseconds")
        // done
        ;

    // all done
    return;
}


// end of file
