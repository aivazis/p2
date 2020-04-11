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
    // metamethods
public:
    inline explicit diagnostic_t(verbosity_type verbosity = 1) :
        pyre::journal::diagnostic_t<diagnostic_t>(verbosity) {}

    // interface
public:
    inline void commit() {}
};


// verify that diagnostics can be instantiated correctly
int main() {
    // make a diagnostic
    diagnostic_t d1;
    // make sure its verbosity is at the default value
    assert (d1.verbosity() == 1);

    // make another diagnostic with a non-default verbosity
    diagnostic_t d2(3);
    // make sure its verbosity is at the default value
    assert (d2.verbosity() == 3);

    // all done
    return 0;
}


// end of file
