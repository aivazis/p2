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

    // verify its name
    assert (channel.name() == "test.channel");
    // its state
    assert (channel.state() == true);
    // and again using the conversion to bool
    assert (channel);
    // verify that the default state is as expected
    assert (channel.defaultState() == true);

    // deactivate it
    channel.deactivate();
    // and check
    assert (channel.state() == false);

    // all done
    return 0;
}


// end of file
