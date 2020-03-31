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
    channel_t channel("test.channel");

    // get its inventory
    auto & inventory = channel.inventory();
    // verify it is on, by default
    assert (inventory.state());
    // and that its device is null
    assert (!inventory.device());

    // all done
    return 0;
}


// end of file
