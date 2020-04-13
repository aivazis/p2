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


// verify a few of the x11 standard colors; the x11 color table is generated automatically from
// the canonical {rgb.txt} file, but stil...
int main() {

    // verify the contents of the {x11} color table
    assert ((ansi_t::x11.at("normal") == csi_t::csi3(0)));
    assert ((ansi_t::x11.at("burlywood") == csi_t::csi24(0xde, 0xb8, 0x87)));
    assert ((ansi_t::x11.at("dark goldenrod") == csi_t::csi24(0xb8, 0x86, 0x0b)));
    assert ((ansi_t::x11.at("dark khaki") == csi_t::csi24(0xbd, 0xb7, 0x6b)));
    assert ((ansi_t::x11.at("dark orange") == csi_t::csi24(0xff, 0x8c, 0x00)));
    assert ((ansi_t::x11.at("dark sea green") == csi_t::csi24(0x8f, 0xbc, 0x8f)));
    assert ((ansi_t::x11.at("firebrick") == csi_t::csi24(0xb2, 0x22, 0x22)));
    assert ((ansi_t::x11.at("hot pink") == csi_t::csi24(0xff, 0x69, 0xb4)));
    assert ((ansi_t::x11.at("indian red") == csi_t::csi24(0xcd, 0x5c, 0x5c)));
    assert ((ansi_t::x11.at("lavender") == csi_t::csi24(0xe6, 0xe6, 0xfa)));
    assert ((ansi_t::x11.at("light green") == csi_t::csi24(0x90, 0xee, 0x90)));
    assert ((ansi_t::x11.at("light steel blue") == csi_t::csi24(0xb0, 0xc4, 0xde)));
    assert ((ansi_t::x11.at("light slate gray") == csi_t::csi24(0x77, 0x88, 0x99)));
    assert ((ansi_t::x11.at("lime green") == csi_t::csi24(0x32, 0xcd, 0x32)));
    assert ((ansi_t::x11.at("navajo white") == csi_t::csi24(0xff, 0xde, 0xad)));
    assert ((ansi_t::x11.at("olive drab") == csi_t::csi24(0x6b, 0x8e, 0x23)));
    assert ((ansi_t::x11.at("peach puff") == csi_t::csi24(0xff, 0xda, 0xb9)));
    assert ((ansi_t::x11.at("steel blue") == csi_t::csi24(0x46, 0x82, 0xb4)));

    // all done
    return 0;
}


// end of file