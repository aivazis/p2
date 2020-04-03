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

// the static data
static ansi_t::table_type make_ansi();
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
