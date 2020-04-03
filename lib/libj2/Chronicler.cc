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
// renderers
#include "Renderer.h"
// support for accessing the console
#include "Device.h"
#include "Stream.h"
#include "Console.h"

// get the declaration
#include "Chronicler.h"

// aliases
using console_t = pyre::journal::cout_t;
using chronicler_t = pyre::journal::chronicler_t;

// helper
static
chronicler_t::metadata_type initializeGlobals();


// data
chronicler_t::metadata_type chronicler_t::_globals = initializeGlobals();
chronicler_t::device_pointer chronicler_t::_device = std::make_shared<console_t>();


// implementation details
chronicler_t::metadata_type initializeGlobals()
{
    // make a table
    chronicler_t::metadata_type table;

    // initialize the expected metadata with default values; applications are expected to
    // replace these with values that are more sensible
    table["application"] = "journal";

    // return it
    return table;
}


// end of file
