// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// externals
#include "external.h"
// namespace setup
#include "forward.h"


// add bindings for the debug channel
void
p2::libjournal::
debug(py::module & m) {

    // type aliases for the member functions (mfp: method pointer)
    // verbosity
    using getVerbosity_mfp = debug_t::verbosity_type (debug_t::*)() const;
    using setVerbosity_mfp = debug_t::verbosity_type (debug_t::*)(debug_t::verbosity_type);
    // state
    using getState_mfp = debug_t::state_type (debug_t::*)() const;
    using setState_mfp = debug_t::state_type (debug_t::*)(debug_t::state_type);
    // device
    using getDevice_mfp = debug_t::device_pointer (debug_t::*)() const;
    using setDevice_mfp = debug_t::device_pointer (debug_t::*)(debug_t::device_pointer);
    // metadata
    using getMetadata_mfp = debug_t::metadata_type & (debug_t::*)() const;


    // the debug channel interface
    py::class_<debug_t>(m, "Debug")
        // the constructor
        .def(py::init<const string_t &>(), "name"_a)

        // accessors
        // the name; read-only property
        .def_property_readonly("name", &debug_t::name)

        // the verbosity level
        .def_property("verbosity",
                      // the getter
                      (getVerbosity_mfp) &debug_t::verbosity,
                      // the setter
                      (setVerbosity_mfp) &debug_t::verbosity,
                      // the docstring
                      "access the verbosity level"
                      )

        // the channel state; mutable property
        .def_property("state",
                      // the getter
                      (getState_mfp) &debug_t::state,
                      // the setter
                      (setState_mfp) &debug_t::state,
                      // the docstring
                      "access the channel activation state"
                      )

        // the registered device: mutable property
        .def_property("device",
                      // the getter
                      (getDevice_mfp) &debug_t::device,
                      // the setter
                      (setDevice_mfp) &debug_t::device,
                      // the docstring
                      "access the output device"
                      )

        // the registered device: read-only property
        .def_property_readonly("meta",
                               // the getter
                               (getMetadata_mfp) &debug_t::metadata,
                               // the docstring
                               "access the channel metadata"
                               )

        // the default state: static read-only property
        .def_property_readonly_static("defaultState",
                                      // the getter
                                      [](py::object) -> debug_t::state_type {
                                          return debug_t::defaultState();
                                      },
                                      // the docstring
                                      "get the default state of debug channels"
                                      )

        // the default device: static mutable property
        .def_property_static("defaultDevice",
                             // the getter
                             [](py::object) -> debug_t::device_pointer {
                                 return debug_t::defaultDevice();
                             },
                             // the setter
                             [](py::object, debug_t::device_pointer device) {
                                 debug_t::defaultDevice(device);
                             },
                             // the docstring
                             "access the default device for all debug channels"
                             )

        // interface
        // activate
        .def("activate", &debug_t::activate, "enable output generation")
        // deactivate
        .def("deactivate", &debug_t::deactivate, "disable output generation")

        // done
        ;

    // all done
    return;
}


// end of file
