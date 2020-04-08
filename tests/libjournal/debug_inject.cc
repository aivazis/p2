// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// verify basic information injection
int main() {
    // make a debug channel
    pyre::journal::debug_t channel("tests.journal.debug");

    // try injecting something into the channel
    channel << "hello world!";
    // get the channel buffer and verify its contents
    assert (channel.buffer() == "hello world!");

    // get the metadata
    auto metadata = channel.metadata();
    // verify that the channel identification entries are present
    assert (metadata["severity"] == "debug");
    assert (metadata["channel"] == "tests.journal.debug");

    // all done
    return 0;
}


// end of file
