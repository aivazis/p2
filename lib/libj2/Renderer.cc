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
    // make a metadata table
    metadata_type local;
    // get the global metadata from the {chronicler_t>
    auto & global = Chronicler::globals();
    // merge them into my local table
    local.insert(std::begin(global), std::end(global));
    // merge the diagnostic metadata as well
    local.insert(std::begin(meta), std::end(meta));

    // make a buffer
    buffer_type buffer;
    // build the document
    header(palette, buffer, page, local);
    body(palette, buffer, page, local);
    footer(palette, buffer, page, local);

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
