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
render(palette_type & palette, const entry_type & entry, const metadata_type & meta) -> string_type
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
    header(palette, buffer, entry, local);
    body(palette, buffer, entry, local);
    footer(palette, buffer, entry, local);

    // extract the string and return it
    return buffer.str();
}


// implementation details
void
pyre::journal::Renderer::
header(palette_type &, buffer_type &, const entry_type &, const metadata_type &)
{
    // all done
    return;
}


void
pyre::journal::Renderer::
body(palette_type &, buffer_type &, const entry_type &, const metadata_type &)
{
    // all done
    return;
}


void
pyre::journal::Renderer::
footer(palette_type &, buffer_type &, const entry_type &, const metadata_type &)
{
    // all done
    return;
}


// end of file
