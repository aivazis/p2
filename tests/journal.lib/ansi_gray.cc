// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>


// type aliases
using csi_t = pyre::journal::csi_t;
using ansi_t = pyre::journal::ansi_t;


// exercise the trivial device
int main() {

    // verify the contents of the {gray} color table
    assert ((ansi_t::gray.at("normal") == csi_t::csi3(0)));
    assert ((ansi_t::gray.at("gray10") == csi_t::csi24(0x19, 0x19, 0x19)));
    assert ((ansi_t::gray.at("gray30") == csi_t::csi24(0x4c, 0x4c, 0x4c)));
    assert ((ansi_t::gray.at("gray41") == csi_t::csi24(0x69, 0x69, 0x69)));
    assert ((ansi_t::gray.at("gray50") == csi_t::csi24(0x80, 0x80, 0x80)));
    assert ((ansi_t::gray.at("gray66") == csi_t::csi24(0xa9, 0xa9, 0xa9)));
    assert ((ansi_t::gray.at("gray75") == csi_t::csi24(0xbe, 0xbe, 0xbe)));

    // all done
    return 0;
}


// end of file
