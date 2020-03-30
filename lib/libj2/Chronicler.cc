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

// support for accessing the console
#include "Device.h"
#include "Stream.h"
#include "Console.h"

// get the declaration
#include "Chronicler.h"

// aliases
using console_t = pyre::journal::console_t;
using chronicler_t = pyre::journal::chronicler_t;


// data
chronicler_t::metadata_type chronicler_t::_globals;
chronicler_t::device_pointer chronicler_t::_device = std::make_shared<console_t>();


// end of file
