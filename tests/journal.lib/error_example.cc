// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// type alias
using myerror_t = pyre::journal::error_t;


// exercise the channel manipulators
int main() {
    // make an error channel
    myerror_t channel("tests.journal.error");

    // deactivate the channel
    channel.deactivate();

    // carefully
    try {
        // inject something into the channel
        channel
            << pyre::journal::at(__HERE__)
            << pyre::journal::set("time", "now")
            << "error channel:" << pyre::journal::newline
            << "    hello world!" << pyre::journal::endl;
        // errors are fatal by default, so we shouldn't be able to get here
        throw std::logic_error("unreachable");
    // if all goes well
    }  catch (const myerror_t::exception_type & error) {
        // make sure the reason was recorded correctly
        assert (error.what() == channel.name() + myerror_t::string_type(": application error"));
    }

    // all done
    return 0;
}


// end of file
