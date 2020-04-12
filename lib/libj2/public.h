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


// implementations
// exceptions
#include "exceptions.h"

// terminal support
#include "ASCII.h"
#include "CSI.h"
#include "ANSI.h"

// abstractions
#include "Renderer.h"
#include "Device.h"

// renderers
#include "Memo.h"
#include "Alert.h"

// the global state
#include "Chronicler.h"

// devices
#include "Trash.h"
#include "Stream.h"
#include "Console.h"
#include "ErrorConsole.h"

// manipulators that are classes
#include "Locator.h"
#include "Selector.h"
#include "Verbosity.h"

// the null diagnostic
#include "Null.h"

// functional diagnostic infrastructure
#include "Index.h"
#include "Inventory.h"
#include "Fatal.h"
#include "Channel.h"
#include "Diagnostic.h"
// the developer facing channels
#include "Debug.h"
#include "Firewall.h"
// the user facing channels
#include "Error.h"
#include "Informational.h"
#include "Warning.h"

// macros
#include "macros.h"

//
inline void
pyre::journal::
init(int argc, char* argv[]) {
    // ask {chronicler} to do this
    pyre::journal::chronicler_t::init(argc, argv);
    // all done
    return;
}


#endif

// end of file
