// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>


// type aliases
using csi_t = pyre::journal::csi_t;
using ansi_t = pyre::journal::ansi_t;
using memo_t = pyre::journal::memo_t;
using debug_t = pyre::journal::debug_t;

#include <iostream>

// verify that the null diagnostic is always off
int main() {
    // use a {debug_t} to build a document and its metdata
    debug_t channel("memo");
    // put some stuff in it; careful not to flush so we don't lose everything
    channel
        << pyre::journal::at(__HERE__)
        << pyre::journal::set("time", "now")
        << "simon says:"
        << pyre::journal::newline
        << "    hello world!"
        << pyre::journal::newline;

    // make a palette
    memo_t::palette_type palette;
    // add some decorations
    palette["reset"] = ansi_t::x11.at("normal");
    palette["channel"] = ansi_t::x11.at("light_slate_gray");
    palette["severity"] = ansi_t::x11.at("light_steel_blue");
    palette["severity"] = csi_t::csi24(0xb0, 0xc4, 0xde);
    palette["filename"] = ansi_t::x11.at("lavender");
    palette["line"] = ansi_t::x11.at("lavender");
    palette["function"] = ansi_t::x11.at("lavender");

    // pull the page
    const memo_t::entry_type & page = channel.entry();
    // and its metadata
    const memo_t::metadata_type & meta = channel.metadata();

    // show me
    std::cout << "meta:" << std::endl;
    for (auto & [key, value]:  meta) {
        std::cout
            << " ++ '" << key << "' -> '"
            << palette[key] << value << palette["reset"] << "'" << std::endl;
    }
    std::cout << "page:" << std::endl;
    for (auto & line: page) {
        std::cout << " -- " << line << std::endl;
    }

    // make a memo
    memo_t memo;
    // ask it to render what we have
    auto msg = memo.render(palette, page, meta);
    // show me
    std::cout << msg << std::endl;

    std::cout
        << csi_t::csi24(0xb0, 0xc4, 0xde)
        << palette["severity"]
        << palette["reset"] << std::endl;

     // nothing to do
    return 0;
}


// end of file
