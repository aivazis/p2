// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// alias
using firewall_t = pyre::journal::firewall_t;


// exercise the channel manipulators
int main() {
    // make a debug channel
    firewall_t channel("tests.journal.firewall");

    // send the output to the trash
    channel.device(std::make_shared<pyre::journal::trash_t>());

    // firewalls are fatal by default, so attempt
    try {
        // inject something into the channel
        channel
            << pyre::journal::at(__HERE__)
            << pyre::journal::note("time", "now")
            << "nasty bug:" << pyre::journal::newline
            << "    hello world!" << pyre::journal::endl;
        // unreachable
        throw std::logic_error("unreachable");
    // if all goes well
    } catch (const firewall_t::exception_type & error) {
        // make sure the reason was recorded correctly
        assert (error.what() == channel.name() + firewall_t::string_type(": FIREWALL BREACHED!"));
    }

    // all done
    return 0;
}


// end of file
