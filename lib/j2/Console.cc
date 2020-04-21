// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the forward declarations
#include "forward.h"
// external support
#include "externals.h"

// support for color
#include "ASCII.h"
#include "CSI.h"
#include "ANSI.h"
// renderer support
#include "Renderer.h"
#include "Memo.h"
#include "Alert.h"
// get the device declarations
#include "Device.h"
#include "Stream.h"
#include "Console.h"

// access {std::cout}
#include <iostream>
// get {isatty}
#include <unistd.h>


// alias
using ansi_t = pyre::journal::ansi_t;


// metamethods
// constructor
pyre::journal::Console::
Console() :
    stream_t("cout", std::cout),
    _tty(isatty(1) == 1)
{
    // if i am connected to a compatible terminal
    if (_tty && ansi_t::compatible())  {
        // populate my palette with some colors
        // put things back to normal
        _palette["reset"] = ansi_t::x11("normal");
        // channel name
        _palette["channel"] = ansi_t::x11("purple");
        // severity
        _palette["info"] = ansi_t::x11("forest green");
        _palette["warning"] = ansi_t::x11("orange");
        _palette["error"] = ansi_t::x11("red");
        _palette["debug"] = ansi_t::x11("cornflower blue");
        _palette["firewall"] = ansi_t::x11("fuchsia");
        // the page body
        _palette["body"] = "";
    }
}


// destructor
pyre::journal::Console::
~Console()
{}


// end of file