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
// get the device declaration
#include "Device.h"
// get the stream declaration
#include "Stream.h"


// metamethods
// destructor
pyre::journal::Stream::
~Stream()
{}


// interface
auto
pyre::journal::Stream::
record(const entry_type & entry, const metadata_type & meta) -> Stream &
{
    // all done
    return *this;
}


// end of file
