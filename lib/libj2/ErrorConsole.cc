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
// access {std::cerr}
#include <iostream>

// get the device declarations
#include "Device.h"
#include "Stream.h"
#include "ErrorConsole.h"


// metamethods
// constructor
pyre::journal::ErrorConsole::
ErrorConsole() :
    stream_t("cerr", std::cerr)
{}


// destructor
pyre::journal::ErrorConsole::
~ErrorConsole()
{}


// end of file
