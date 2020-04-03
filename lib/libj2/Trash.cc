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
// get the device declaration
#include "Device.h"
// get the stream declaration
#include "Trash.h"


// metamethods
// destructor
pyre::journal::Trash::
~Trash()
{}


// interface
auto
pyre::journal::Trash::
memo(const entry_type &, const metadata_type &) -> Trash &
{
    // all done
    return *this;
}


auto
pyre::journal::Trash::
alert(const entry_type &, const metadata_type &) -> Trash &
{
    // all done
    return *this;
}


// end of file
