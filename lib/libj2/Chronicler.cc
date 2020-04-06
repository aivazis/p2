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
// renderer support
#include "Renderer.h"
#include "Memo.h"
#include "Alert.h"
// support for accessing the console
#include "Device.h"
#include "Stream.h"
#include "Console.h"

// get the declaration
#include "Chronicler.h"

// aliases
using console_t = pyre::journal::cout_t;
using chronicler_t = pyre::journal::chronicler_t;

// helpers
static chronicler_t::metadata_type initializeGlobals();
static chronicler_t::verbosity_type initializeVerbosity();


// data
chronicler_t::verbosity_type chronicler_t::_verbosity = initializeVerbosity();
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


chronicler_t::verbosity_type initializeVerbosity()
{
    // establish the default severity level
    pyre::journal::verbosity_t level = 1;

    // read the {JOURNAL_VERB} environment variable
    auto setting = std::getenv("JOURNAL_VERBOSITY");
    // if it doesn't exist
    if (setting == nullptr) {
        // go with our default
        return level;
    }
    // otherwise, attempt to convert to a {verbosity_t}
    auto status = std::strtol(setting, nullptr, 10);
    // if the conversion failed
    if (status == 0) {
        // go with our default
        return level;
    }

    // otherwise, use the converted value as the new level; note that this implementation makes
    // it impossible to set the verbosity level to zero from the environment
    return status;
}


// end of file
