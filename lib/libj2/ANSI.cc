// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the forward declarations
#include "forward.h"
// external support
#include "externals.h"
// get the support we need
#include "ASCII.h"
#include "CSI.h"
#include "ANSI.h"


// type aliases
using csi_t = pyre::journal::csi_t;
using ansi_t = pyre::journal::ansi_t;


// the set compatible emulations
static
std::set<std::string>
compatible { "ansi",
             "vt102", "vt220", "vt320", "vt420",
             "xterm", "xterm-color", "xterm-16color", "xterm-256color" };


// the helpers
static bool emulates();

static ansi_t::table_type make_ansi();
static ansi_t::table_type make_x11();
static ansi_t::table_type make_gray();
static ansi_t::table_type make_misc();


// the emulation predicate
bool ansi_t::compatible()
{
    // check; once and only once
    static bool flag = emulates();
    // and return the result
    return flag;
}


// the static objects in {ansi_t}
ansi_t::table_type ansi_t::null;
ansi_t::table_type ansi_t::ansi = make_ansi();
ansi_t::table_type ansi_t::x11 = make_x11();
ansi_t::table_type ansi_t::gray = make_gray();
ansi_t::table_type ansi_t::misc = make_misc();


// implementations
bool emulates()
{
    // get the {TERM} environment variable
    auto term = std::getenv("TERM");
    // if the value is not set
    if (term == nullptr) {
        // we don't know, so better be safe
        return false;
    }

    // if the value is not in the set of supported emulations
    if (compatible.find(term) == compatible.end()) {
        // report failure
        return false;
    }

    // otherwise, all good
    return true;
}


ansi_t::table_type make_ansi()
{
    // make a table
    ansi_t::table_type table;

    // the reset sequence
    table["normal"] = csi_t::csi3(0);

    // regular colors
    table["black"] = csi_t::csi3(30);
    table["red"] = csi_t::csi3(31);
    table["green"] = csi_t::csi3(32);
    table["brown"] = csi_t::csi3(33);
    table["blue"] = csi_t::csi3(34);
    table["purple"] = csi_t::csi3(35);
    table["cyan"] = csi_t::csi3(36);
    table["light-gray"] = csi_t::csi3(37);

    // bright colors
    table["dark-gray"] = csi_t::csi3(30, true);
    table["light-red"] = csi_t::csi3(31, true);
    table["light-green"] = csi_t::csi3(32, true);
    table["yellow"] = csi_t::csi3(33, true);
    table["light-blue"] = csi_t::csi3(34, true);
    table["light-purple"] = csi_t::csi3(35, true);
    table["light-cyan"] = csi_t::csi3(36, true);
    table["white"] = csi_t::csi3(37, true);

    // all done
    return table;
}


ansi_t::table_type make_x11()
{
    // make a table
    ansi_t::table_type table;

    // the reset sequence
    table["normal"] = csi_t::csi3(0);

    // the X11 named colors
    table["burlywood"] = csi_t::csi24(0xde, 0xb8, 0x87);
    table["dark_goldenrod"] = csi_t::csi24(0xb8, 0x86, 0x0b);
    table["dark_khaki"] = csi_t::csi24(0xbd, 0xb7, 0x6b);
    table["dark_orange"] = csi_t::csi24(0xff, 0x8c, 0x00);
    table["dark_sea_green"] = csi_t::csi24(0x8f, 0xbc, 0x8f);
    table["firebrick"] = csi_t::csi24(0xb2, 0x22, 0x22);
    table["hot_pink"] = csi_t::csi24(0xff, 0x69, 0xb4);
    table["indian_red"] = csi_t::csi24(0xcd, 0x5c, 0x5c);
    table["lavender"] = csi_t::csi24(0xc0, 0xb0, 0xe0);
    table["light_green"] = csi_t::csi24(0x90, 0xee, 0x90);
    table["light_steel_blue"] = csi_t::csi24(0xb0, 0xc4, 0xde);
    table["light_slate_gray"] = csi_t::csi24(0x77, 0x88, 0x99);
    table["lime_green"] = csi_t::csi24(0x32, 0xcd, 0x32);
    table["navajo_white"] = csi_t::csi24(0xff, 0xde, 0xad);
    table["olive_drab"] = csi_t::csi24(0x6b, 0x8e, 0x23);
    table["peach_puff"] = csi_t::csi24(0xff, 0xda, 0xb9);
    table["sage"] = csi_t::csi24(176, 208, 176);
    table["steel_blue"] = csi_t::csi24(0x46, 0x82, 0xb4);

    // all done
    return table;
}


ansi_t::table_type make_gray()
{
    // make a table
    ansi_t::table_type table;

    // the reset sequence
    table["normal"] = csi_t::csi3(0);

    // grays
    table["gray10"] = csi_t::csi24(0x19, 0x19, 0x19);
    table["gray30"] = csi_t::csi24(0x4c, 0x4c, 0x4c);
    table["gray41"] = csi_t::csi24(0x69, 0x69, 0x69);
    table["gray50"] = csi_t::csi24(0x80, 0x80, 0x80);
    table["gray66"] = csi_t::csi24(0xa9, 0xa9, 0xa9);
    table["gray75"] = csi_t::csi24(0xbe, 0xbe, 0xbe);

    // all done
    return table;
}


ansi_t::table_type make_misc()
{
    // make a table
    ansi_t::table_type table;

    // the reset sequence
    table["normal"] = csi_t::csi3(0);

    // other custom colors
    table["amber"] = csi_t::csi24(0xff, 0xbf, 0x00);

    // all done
    return table;
}


// end of file
