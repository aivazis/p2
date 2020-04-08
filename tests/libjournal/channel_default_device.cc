// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// type aliases
template <bool stateV = true>
using inventory_t = pyre::journal::inventory_t<stateV>;

template <typename severityT, typename inventoryT>
using channel_t = pyre::journal::channel_t<severityT, inventoryT>;


// severity stub
class severity_t :
    public channel_t<severity_t, inventory_t<true>>
{
    // types
public:
    using channel_type = channel_t<severity_t, inventory_t<true>>;

    // metamethods
public:
    // index initialization is required...
    severity_t(const name_type &);
};

// stub implementation
severity_t::severity_t(const name_type & name) :
    channel_type(name)
{}

// the trash can
using trash_t = pyre::journal::trash_t;


// verify that the chronicler is accessible
int main() {
    // get the default device
    auto builtin = severity_t::defaultDevice();

    // make a new device
    auto custom = std::make_shared<trash_t>();
    // install it
    auto old = severity_t::defaultDevice(custom);

    // check that the current device is the one we just installed
    assert (severity_t::defaultDevice().get() == custom.get());
    // and that the device returned during installation is the {builtin} one
    assert (old.get() == builtin.get());

    // all done
    return 0;
}


// end of file
