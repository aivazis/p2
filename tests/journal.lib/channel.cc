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
    severity_t channel("test.channel");

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
