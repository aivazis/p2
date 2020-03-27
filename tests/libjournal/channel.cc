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
    using string_t = std::string;
    using name_t = string_t;
    using inventory_t = pyre::journal::inventory_t<true>;
    using index_t = pyre::journal::index_t<inventory_t>;

    // interface
public:
    inline static auto lookup(const name_t &) -> inventory_t &;

    // data
private:
    // the index
    static index_t _index;
};

// implementation
auto
severity::lookup(const name_t & name) -> inventory_t &
{
    // easy enough
    return _index.lookup(name);
}

// the static index
severity::index_t severity::_index;


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
    // verify that there is no registered device
    assert (channel.device() == nullptr);

    // deactivate it
    channel.deactivate();
    // and check
    assert (channel.state() == false);

    // all done
    return 0;
}


// end of file
