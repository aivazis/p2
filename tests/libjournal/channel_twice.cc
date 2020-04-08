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


// exercise the channel state interface
int main() {
    // make a channel
    severity_t channel_1("test.channel");
    // verify it's on
    assert (channel_1);
    // deactivate it
    channel_1.deactivate();
    // and check
    assert (!channel_1);

    // access again through another variable
    severity_t channel_2("test.channel");
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
