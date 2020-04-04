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
// the trash can
using trash_t = pyre::journal::trash_t;
// the chronicler
using chronicler_t = pyre::journal::chronicler_t;
// channel realization
using channel_t = pyre::journal::channel_t<severity, pyre::journal::inventory_t<true>>;


// verify that the chronicler is accessible
int main() {
    // make a trash can
    auto trash = std::make_shared<trash_t>();
    // ask the chronicler for its device
    auto global = chronicler_t::device();

    // make a couple of channels
    channel_t channel_1("journal.tests.channel_1");
    channel_t channel_2("journal.tests.channel_2");

    // by default, we should be getting the global setting from the chronicler
    assert (channel_1.device() == global);
    assert (channel_2.device() == global);

    // set the channel-wide default
    channel_t::defaultDevice(trash);
    // and get it back
    auto shared = channel_t::defaultDevice();
    // verify that that's what the channels see
    assert (channel_1.device() == shared);
    assert (channel_2.device() == shared);

    // set the channel specific devices for both of them to different devices
    channel_1.device(std::make_shared<trash_t>());
    channel_2.device(std::make_shared<trash_t>());
    // verify that the two channels  now have different devices
    assert (channel_1.device() != channel_2.device());

    // make a channel that shares state with {channel_1}
    channel_t channel_10("journal.tests.channel_1");
    // verify it has the same device
    assert (channel_10.device() == channel_1.device());

    // repeat with {channel_2}
    channel_t channel_20("journal.tests.channel_2");
    assert (channel_20.device() == channel_2.device());

    // and that the two new channels have different devices
    assert (channel_10.device() != channel_20.device());

    // all done
    return 0;
}


// end of file
