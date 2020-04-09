// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// standard library
#include <string>


// pybind support
#include <pybind11/pybind11.h>
// get the special {pybind11} literals
using namespace pybind11::literals;


// get the journal
#include <p2/journal.h>


// type aliases
namespace p2::libjournal {
    // from the standard library
    using string_t = std::string;


    // from {pybind11}
    namespace py = pybind11;


    // from {pyre::journal}
    // devices
    using device_t = pyre::journal::device_t;
    using trash_t = pyre::journal::trash_t;
    using stream_t = pyre::journal::stream_t;
    using cout_t = pyre::journal::cout_t;
    using cerr_t = pyre::journal::cerr_t;

    // channels
    using debug_t = pyre::journal::debug_t;
    using firewall_t = pyre::journal::firewall_t;
    using info_t = pyre::journal::info_t;
    using warning_t = pyre::journal::warning_t;
    using error_t = pyre::journal::error_t;
}


// end of file
