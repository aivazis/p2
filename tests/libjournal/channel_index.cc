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


// exercise the channel state index
int main() {
    // make a couple of channels
    channel_t channel_1("test.channel_1");
    channel_t channel_2("test.channel_2");

    // get the index through the first channel
    const channel_t::index_type & index_1 = channel_1.index();
    // verify it has exactly two channels
    assert (index_1.size() == 2);
    // one of them is "test.channel1"
    assert (index_1.contains("test.channel_1"));
    // and the other is "test.channel2"
    assert (index_1.contains("test.channel_2"));

    // get the index through the second channel
    const channel_t::index_type & index_2 = channel_2.index();
    // verify it has exactly two channels
    assert (index_2.size() == 2);
    // one of them is "test.channel1"
    assert (index_2.contains("test.channel_1"));
    // and the other is "test.channel2"
    assert (index_2.contains("test.channel_2"));

    // all done
    return 0;
}


// end of file
