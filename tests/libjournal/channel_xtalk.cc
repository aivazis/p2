// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>


// info
class info {};
using info_t = pyre::journal::channel_t<info, pyre::journal::inventory_t<false>>;

// warning
class warning {};
using warning_t = pyre::journal::channel_t<warning, pyre::journal::inventory_t<true>>;

// error
class error {};
using error_t = pyre::journal::channel_t<error, pyre::journal::inventory_t<true>>;


// verify there is no crosstalk among the indices of different severities
int main() {
    // make a couple of info channels
    info_t info_1("info.channel_1");
    info_t info_2("info.channel_2");
    // a couple of warning channels
    warning_t warning_1("warning.channel_1");
    warning_t warning_2("warning.channel_2");
    // and a couple of error channels
    error_t error_1("error.channel_1");
    error_t error_2("error.channel_2");

    // check the states
    assert (!info_1);
    assert (!info_2);
    assert (warning_1);
    assert (warning_2);
    assert (error_1);
    assert (error_2);

    // get the info index
    const info_t::index_type & infos = info_1.index();
    // verify it has exactly two channels
    assert (infos.size() == 2);
    // one of them is "test.channel1"
    assert (infos.contains("info.channel_1"));
    // and the other is "test.channel2"
    assert (infos.contains("info.channel_2"));

    // get the warning index
    const warning_t::index_type & warnings = warning_1.index();
    // verify it has exactly two channels
    assert (warnings.size() == 2);
    // one of them is "test.channel1"
    assert (warnings.contains("warning.channel_1"));
    // and the other is "test.channel2"
    assert (warnings.contains("warning.channel_2"));

    // get the error index
    const error_t::index_type & errors = error_1.index();
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
