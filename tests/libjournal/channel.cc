// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>
#include <iostream>


// severity stub
class severity {
    // types
public:
    using string_type = std::string;
    using name_type = string_type;
    using inventory_type = pyre::journal::inventory_t<true>;
    using index_type = pyre::journal::index_t<inventory_type>;

    // interface
public:
    inline static auto lookup(const name_type &) -> inventory_type &;

    // data
private:
    // the index
    static index_type _index;
};

// implementation
auto
severity::lookup(const name_type & name) -> inventory_type &
{
    // easy enough
    return _index.lookup(name);
}

// the static index
severity::index_type severity::_index;


// channel realization
using channel_t = pyre::journal::channel_t<severity>;


// exercise the channel state index
int main() {
    // make an index
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
