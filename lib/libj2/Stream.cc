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
memo(const entry_type &, const metadata_type &) -> Stream &
{
    // all done
    return *this;
}


auto
pyre::journal::Stream::
alert(const entry_type &, const metadata_type &) -> Stream &
{
    // all done
    return *this;
}


// end of file
