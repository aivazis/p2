// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
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
        << std::setw(15)
        << "hello world!"
        << pyre::journal::newline;

    // check the entry
    for (auto value : diagnostic.page()) {
        // verify that there is only one value and it is what we expect
        assert (value == "   hello world!");
    }

    // all done
    return 0;
}


// end of file
