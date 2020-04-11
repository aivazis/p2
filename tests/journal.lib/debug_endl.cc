// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// verify that flushing the channel resets its buffers correctly
int main() {
    // make a debug channel
    pyre::journal::debug_t channel("tests.journal.debug");

    // activate it
    // channel.activate();

    // try injecting something into the channel
    channel
        << pyre::journal::at(__HERE__)
        << pyre::journal::set("time", "now")
        << "    hello world!" << pyre::journal::endl;

    // verify that the buffer is empty
    assert (channel.buffer().empty());
    // the page is empty
    assert (channel.page().empty());
    // but the metadata has been retained
    assert (!channel.metadata().empty());

    // all done
    return 0;
}


// end of file
