// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// the {libjournal} namespace
namespace p2::libjournal {

    // bindings of opaque types
    void opaque(py::module &);
    // module methods
    void chronicler(py::module &);
    void devices(py::module &);

    // developer channels
    void debug(py::module &);
    // user facing channels
    void info(py::module &);
}


// end of file
