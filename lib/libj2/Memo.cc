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

// support for color
#include "ASCII.h"
#include "CSI.h"
// access to the type names
#include "Device.h"
// the superclass
#include "Renderer.h"
// the declaration
#include "Memo.h"


// metamethods
pyre::journal::Memo::
~Memo()
{}


// implementation details
void
pyre::journal::Memo::
header(palette_type &, buffer_type &, const entry_type &, const metadata_type &)
{
    // all done
    return;
}


void
pyre::journal::Memo::
body(palette_type &, buffer_type &, const entry_type &, const metadata_type &)
{
    // all done
    return;
}


// end of file
