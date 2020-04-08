// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// severity stub
class diagnostic_t : public pyre::journal::diagnostic_t<diagnostic_t> {
    // interface
public:
    inline void commit() {}
};


// exercise the manipulators
int main() {
    // make a diagnostic
    diagnostic_t diagnostic;

    // inject something; avoid flushing by using {endl}
    diagnostic
        << pyre::journal::at(__HERE__)
        << pyre::journal::verbosity(4)
        << pyre::journal::set("time", "now")
        << "hello world!" << pyre::journal::newline;

    // verify the verbosity level
    assert (diagnostic.verbosity() == 4);

    // get the metadata
    auto meta = diagnostic.metadata();
    // verify that our decorations are present
    assert (meta["filename"] == __FILE__);
    assert (meta["line"] == "28");
    assert (meta["function"] == __func__);
    assert (meta["time"] == "now");

    // all done
    return 0;
}


// end of file
