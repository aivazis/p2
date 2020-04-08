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


// exercise the diagnostic state index
int main() {
    // make a diagnostic
    diagnostic_t diagnostic;

    // inject something
    diagnostic
        << pyre::journal::at(__HERE__)
        << pyre::journal::set("time", "now")
        << "hello world!" << pyre::journal::newline
        << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
