// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>
// support
#include <cassert>


// type aliases
using csi_t = pyre::journal::csi_t;
using ansi_t = pyre::journal::ansi_t;


// exercise the trivial device
int main() {

    // verify the contents of the {misc} color table
    assert ((ansi_t::misc.at("normal") == csi_t::csi3(0)));
    assert ((ansi_t::misc.at("amber") == csi_t::csi24(0xff, 0xbf, 0x00)));

    // all done
    return 0;
}


// end of file
