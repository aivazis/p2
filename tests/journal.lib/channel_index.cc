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


// exercise the channel state index
int main() {
    // make a couple of channels
    severity_t channel_1("test.channel_1");
    severity_t channel_2("test.channel_2");

    // get the index through the first channel
    const severity_t::index_type & index_1 = channel_1.index();
    // verify it has exactly two channels
    assert (index_1.size() == 2);
    // one of them is "test.channel1"
    assert (index_1.contains("test.channel_1"));
    // and the other is "test.channel2"
    assert (index_1.contains("test.channel_2"));

    // get the index through the second channel
    const severity_t::index_type & index_2 = channel_2.index();
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
