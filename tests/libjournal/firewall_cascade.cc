// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>


// type aliases
// chronicler
using chronicler_t = pyre::journal::chronicler_t;
// firewall
using firewall_t = pyre::journal::firewall_t;
// the trash can
using trash_t = pyre::journal::trash_t;


// exercise the channel state index
int main() {
    // make a channel
    firewall_t parent("test.firewall.parent");
    // its activation state is what's expected
    assert(parent.state());
    // it is fatal
    assert(parent.fatal());
    // and the device is null
    assert(parent.device() == chronicler_t::device());
    // turn it off
    parent.deactivate();
    // make it non-fatal
    parent.fatal(false);
    // and set the device to a trash can
    parent.device(std::make_shared<trash_t>());

    // make a firewall that's lower in the hierarchy
    firewall_t child("test.firewall.parent.blah.blah.child");
    // make sure its activation state is what's expected
    assert(child.state() == parent.state());
    // it is also non-fatal
    assert(child.fatal() == parent.fatal());
    // and that it inherited the device
    assert(child.device() == parent.device());

    // all done
    return 0;
}


// end of file
