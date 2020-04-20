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
memo(verbosity_type, const page_type & page, const metadata_type & meta) -> Trash &
{
    // make an empty palette
    palette_type palette;
    // go through the motions, and then discard the content
    _memo->render(palette, page, meta);
    // all done
    return *this;
}


auto
pyre::journal::Trash::
alert(verbosity_type, const page_type & page, const metadata_type & meta) -> Trash &
{
    // make an empty palette
    palette_type palette;
    // go through the motions, and then discard the content
    _alert->render(palette, page, meta);
    // all done
    return *this;
}


// end of file
