// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// for the build system
#include <portinfo>
// get the forward declarations
#include "forward.h"
// external support
#include "externals.h"
// access {std::cout}
#include <iostream>

// get the device declarations
#include "Device.h"
#include "Stream.h"
#include "Console.h"


// metamethods
// constructor
pyre::journal::Console::
Console() :
    stream_t("console", std::cout)
{}


// destructor
pyre::journal::Console::
~Console()
{}


// end of file
