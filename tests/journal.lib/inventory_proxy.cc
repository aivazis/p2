// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// verify that we can create two proxies to the same shared inventory and manipulate the
// shared state through either one


// the journal
#include <p2/journal.h>
// support
#include <cassert>


// convenience
template <class clientT>
using proxy_t = pyre::journal::inventory_proxy_t<clientT>;


// a client stub; the proxy relies on {crtp} to enable chaining
class channel_t : public proxy_t<channel_t>
{
    // type aliases
public:
    using proxy_type = proxy_t<channel_t>;
    using inventory_type = typename proxy_type::inventory_type;
    using inventory_reference = typename proxy_type::inventory_reference;

    // metamethods
public:
    inline channel_t(inventory_reference inventory) :
        proxy_type(inventory)
    {}
};


// verify that we can manipulate the inventory state through a proxy
int main() {
    // make the shared inventory instance
    channel_t::inventory_type inventory(true, false);

    // create a channel
    channel_t ch_1(inventory);
    // check that the client sees the state of the inventory
    assert (ch_1.active() == inventory.active());
    assert (ch_1.fatal() == inventory.fatal());
    assert (ch_1.device() == inventory.device());

    // create another channel with access to the shared state
    channel_t ch_2(inventory);
    // repeat
    assert (ch_2.active() == inventory.active());
    assert (ch_2.fatal() == inventory.fatal());
    assert (ch_2.device() == inventory.device());

    // do some damage through {ch_1}
    ch_1.active(false).fatal(true);

    // verify
    assert (ch_1.active() == ch_2.active());
    assert (ch_1.fatal() == ch_2.fatal());

    // do some damage through {ch_2}
    ch_1.active(true).fatal(false);

    // verify
    assert (ch_1.active() == ch_2.active());
    assert (ch_1.fatal() == ch_2.fatal());

    // all done
    return 0;
}


// end of file
