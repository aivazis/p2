// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>

// support
#include <cassert>


// convenience
using inventory_t = pyre::journal::firewall_t::inventory_type;

// verify that we can manipulate the inventory state at runtime
int main() {
    // make a default inventory
    inventory_t firewall;
    // by default, its device is null
    assert(firewall.device().get() == nullptr);

    // verify the default state is on
    assert(firewall.defaultState() == true);
    // verify it is on
    assert(firewall.state() == true);
    // flip it
    firewall.deactivate();
    // check again
    assert(firewall.state() == false);

    // verify it's fatal by default
    assert(firewall.fatal() == true);
    // flip it
    firewall.fatal(false);
    // check again
    assert(firewall.fatal() == false);

    // all done
    return 0;
}


// end of file
