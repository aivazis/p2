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
// renderer
#include "Renderer.h"
// the device declarations
#include "Device.h"
#include "Stream.h"
#include "ErrorConsole.h"

// access {std::cerr}
#include <iostream>
// get {isatty}
#include <unistd.h>


// metamethods
// constructor
pyre::journal::ErrorConsole::
ErrorConsole() :
    stream_t("cerr", std::cerr),
    _tty(isatty(2) == 1)
{}


// destructor
pyre::journal::ErrorConsole::
~ErrorConsole()
{}


// end of file
