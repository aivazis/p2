// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the forward declarations
#include "forward.h"
// external support
#include "externals.h"

// access to color support
#include "ASCII.h"
#include "CSI.h"
// access to the type names
#include "Device.h"
// access to the gloabal state
#include "Chronicler.h"

// get the declaration
#include "Renderer.h"


// metamethods
pyre::journal::Renderer::
~Renderer()
{}


// interface
auto
pyre::journal::Renderer::
render(palette_type & palette, const page_type & page,
       const metadata_type & meta) const -> bufmsg_type
{
    // make a buffer
    buffer_type buffer;

    // build the document
    header(palette, buffer, page, meta);
    body(palette, buffer, page, meta);
    footer(palette, buffer, page, meta);

    // extract the string and return it
    return buffer.str();
}


// implementation details
void
pyre::journal::Renderer::
header(palette_type &, buffer_type &, const page_type &, const metadata_type &) const
{
    // all done
    return;
}


void
pyre::journal::Renderer::
body(palette_type &, buffer_type &, const page_type &, const metadata_type &) const
{
    // all done
    return;
}


void
pyre::journal::Renderer::
footer(palette_type &, buffer_type &, const page_type &, const metadata_type &) const
{
    // all done
    return;
}


// end of file
