// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>


// exercise the channel manipulators
int main() {
    // make a debug channel
    pyre::journal::debug_t channel("tests.journal.debug");

    // activate it
    channel.activate();

    // try injecting something into the channel
    channel
        << pyre::journal::at(__HERE__)
        << pyre::journal::set("time", "now")
        << "    hello world!" << pyre::journal::endl;

    // verify that the buffer is empty
    assert (channel.buffer().empty());
    // the page is empty
    assert (channel.page().empty());
    // the metadata has been flushed
    assert (channel.metadata().empty());

    // all done
    return 0;
}


// end of file
