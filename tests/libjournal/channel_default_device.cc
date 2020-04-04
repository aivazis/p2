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
// the trash can
using trash_t = pyre::journal::trash_t;

// verify that the chronicler is accessible
int main() {
    // get the default device
    auto builtin = channel_t::defaultDevice();

    // make a new device
    auto custom = std::make_shared<trash_t>();
    // install it
    auto old = channel_t::defaultDevice(custom);

    // check that the current device is the one we just installed
    assert (channel_t::defaultDevice().get() == custom.get());
    // and that the device returned during installation is the {builtin} one
    assert (old.get() == builtin.get());

    // all done
    return 0;
}


// end of file
