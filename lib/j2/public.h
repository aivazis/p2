// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_public_h)
#define pyre_journal_public_h


// external packages
#include "externals.h"
// get the forward declarations
#include "forward.h"

// published type aliases; this is the file you are looking for...
#include "api.h"

// exceptions
#include "exceptions.h"

// global settings
#include "Chronicler.h"

// message entry
#include "Entry.h"
// message metadata
#include "Verbosity.h"
#include "Locator.h"
#include "Note.h"
#include "Flush.h"

// abstractions
#include "Renderer.h"
#include "Device.h"

// renderers
#include "Alert.h"
#include "Memo.h"

// devices
#include "Trash.h"
#include "File.h"
#include "Stream.h"
#include "Console.h"
#include "ErrorConsole.h"

// support for channel shared state
#include "Inventory.h"
#include "InventoryProxy.h"
#include "Index.h"

// channel infrastructure
#include "Channel.h"

// channels
#include "Null.h"
// end user facing
#include "Informational.h"
#include "Warning.h"
#include "Error.h"
// developer facing
#include "Debug.h"
#include "Firewall.h"

// manipulators
#include "manipulators.h"

// terminal support
#include "ASCII.h"
#include "CSI.h"
#include "ANSI.h"


// the convenience initializer
void
pyre::journal::
init(int argc, char* argv[])
{
    // ask {chronicler} to do this
    pyre::journal::chronicler_t::init(argc, argv);
    // all done
    return;
}


// install the trash can as the global device
void
pyre::journal::
quiet()
{
    // forward to the {chronicler_t}
    chronicler_t::quiet();
    // all done
    return;
}


#endif

// end of file
