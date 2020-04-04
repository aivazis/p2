// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>


// alias
using firewall_t = pyre::journal::firewall_t;


// exercise the channel manipulators
int main() {
    // make a debug channel
    firewall_t channel("tests.journal.firewall");

    // suppress the output to the screen
    channel.deactivate();
    // make sure the firewall isn't fatal
    channel.fatal(false);

    // firewalls are fatal by default, so attempt
    try {
        // inject something into the channel
        channel
            << pyre::journal::at(__HERE__)
            << pyre::journal::set("time", "now")
            << "nasty bug:" << pyre::journal::newline
            << "    hello world!" << pyre::journal::endl;
    // if the firewall triggered the exception
    } catch (const firewall_t::exception_type & error) {
        // unreachable
        throw std::logic_error("unreachable");
    }

    // all done
    return 0;
}


// end of file
