// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// channel stub
class channel_t : public pyre::journal::channel_t<channel_t> {
    // metamethods
public:
    inline explicit channel_t(const name_type & name) :
        pyre::journal::channel_t<channel_t>(name) {}
};


// verify that the message is assembled correctly
int main() {
    // make a channel
    channel_t channel("channel");

    // inject something
    channel
        << std::setw(15)
        << "hello world!"
        << pyre::journal::newline;

    // check the entry
    for (auto value : channel.entry().page()) {
        // verify that there is only one value and it is what we expect
        assert (value == "   hello world!");
    }

    // all done
    return 0;
}


// end of file