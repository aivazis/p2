// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>


// type aliases
template <bool stateV = true>
using inventory_t = pyre::journal::inventory_t<stateV>;

template <typename severityT, typename inventoryT>
using channel_t = pyre::journal::channel_t<severityT, inventoryT>;


// severity stubs
// info
class myinfo_t :
    public channel_t<myinfo_t, inventory_t<false>>
{
    // types
public:
    using channel_type = channel_t<myinfo_t, inventory_t<false>>;

    // metamethods
public:
    // index initialization is required...
    myinfo_t(const name_type &);
};

// info stub implementation
myinfo_t::myinfo_t(const name_type & name) :
    channel_type(name)
{}


// warning
class mywarning_t :
    public channel_t<mywarning_t, inventory_t<true>>
{
    // types
public:
    using channel_type = channel_t<mywarning_t, inventory_t<true>>;

    // metamethods
public:
    // index initialization is required...
    mywarning_t(const name_type &);
};

// warning stub implementation
mywarning_t::mywarning_t(const name_type & name) :
    channel_type(name)
{}


// error
class myerror_t :
    public channel_t<myerror_t, inventory_t<true>>
{
    // types
public:
    using channel_type = channel_t<myerror_t, inventory_t<true>>;

    // metamethods
public:
    // index initialization is required...
    myerror_t(const name_type &);
};

// error stub implementation
myerror_t::myerror_t(const name_type & name) :
    channel_type(name)
{}


// verify there is no crosstalk among the indices of different severities
int main() {
    // make a couple of info channels
    myinfo_t info_1("info.channel_1");
    myinfo_t info_2("info.channel_2");
    // a couple of warning channels
    mywarning_t warning_1("warning.channel_1");
    mywarning_t warning_2("warning.channel_2");
    // and a couple of error channels
    myerror_t error_1("error.channel_1");
    myerror_t error_2("error.channel_2");

    // check the states
    assert (!info_1);
    assert (!info_2);
    assert (warning_1);
    assert (warning_2);
    assert (error_1);
    assert (error_2);

    // get the info index
    const myinfo_t::index_type & infos = info_1.index();
    // verify it has exactly two channels
    assert (infos.size() == 2);
    // one of them is "test.channel1"
    assert (infos.contains("info.channel_1"));
    // and the other is "test.channel2"
    assert (infos.contains("info.channel_2"));

    // get the warning index
    const mywarning_t::index_type & warnings = warning_1.index();
    // verify it has exactly two channels
    assert (warnings.size() == 2);
    // one of them is "test.channel1"
    assert (warnings.contains("warning.channel_1"));
    // and the other is "test.channel2"
    assert (warnings.contains("warning.channel_2"));

    // get the error index
    const myerror_t::index_type & errors = error_1.index();
    // verify it has exactly two channels
    assert (errors.size() == 2);
    // one of them is "test.channel1"
    assert (errors.contains("error.channel_1"));
    // and the other is "test.channel2"
    assert (errors.contains("error.channel_2"));

    // all done
    return 0;
}


// end of file
