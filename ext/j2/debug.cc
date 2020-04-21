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

        // static interface
        // the default state
        .def_static("defaultState", &debug_t::defaultState)
        // the default device
        .def_static("defaultDevice", (debug_t::device_pointer (*)()) &debug_t::defaultDevice)
        // done
        ;

    // all done
    return;
}


// end of file
