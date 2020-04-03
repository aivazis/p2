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
// get the device declarations
#include "Device.h"
#include "Stream.h"
#include "Console.h"

// access {std::cout}
#include <iostream>
// get {isatty}
#include <unistd.h>


// metamethods
// constructor
pyre::journal::Console::
Console() :
    stream_t("cout", std::cout),
    _tty(isatty(1) == 1)
{}


// destructor
pyre::journal::Console::
~Console()
{}


// end of file
