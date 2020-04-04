// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>


// severity stub
class severity {};
// channel realization
using channel_t = pyre::journal::channel_t<severity, pyre::journal::inventory_t<true>>;


// exercise the channel state interface
int main() {
    // make a channel
    channel_t channel_1("test.channel");
    // verify it's on
    assert (channel_1);
    // deactivate it
    channel_1.deactivate();
    // and check
    assert (!channel_1);

    // access again through another variable
    channel_t channel_2("test.channel");
    // verify it's off
    assert (!channel_2);
    // activate it
    channel_2.activate();
    // check
    assert (channel_2);
    // verify that {channel_1} mirrors the new settings
    assert (channel_1);

    // all done
    return 0;
}


// end of file
