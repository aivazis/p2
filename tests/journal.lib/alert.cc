// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>


// type aliases
using csi_t = pyre::journal::csi_t;
using ansi_t = pyre::journal::ansi_t;
using alert_t = pyre::journal::alert_t;
using debug_t = pyre::journal::debug_t;
using chronicler_t = pyre::journal::chronicler_t;


// exercise the {alert} renderer
int main() {
    // grab the global metadata table from chronicler
    auto & globals = chronicler_t::globals();
    // set some metadata
    globals["application"] = "alert";
    globals["author"] = "michael";

    // use a {debug_t} to build a document and its metdata
    debug_t channel("alert");
    // put some stuff in it; careful not to flush so we don't lose everything
    channel
        << pyre::journal::at(__HERE__)
        << pyre::journal::set("time", "now")
        << pyre::journal::set("device", "null")
        << "simon says:"
        << pyre::journal::newline
        << "hello world!"
        << pyre::journal::newline;

    // make a palette
    alert_t::palette_type palette;
    // add some decorations
    palette["reset"] = ansi_t::x11.at("normal");
    palette["channel"] = ansi_t::x11.at("light slate gray");
    palette["debug"] = ansi_t::x11.at("steel blue");
    palette["body"] = "";

    // pull the page
    auto & page = channel.page();
    // and its metadata
    auto & meta = channel.metadata();

    // make an alert
    alert_t alert;
    // ask it to render what we have
    alert.render(palette, page, meta);

    // all done
    return 0;
}


// end of file
