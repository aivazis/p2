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
#include "Alert.h"


// metamethods
pyre::journal::Alert::
~Alert()
{}


// implementation details
void
pyre::journal::Alert::
header(palette_type & palette, buffer_type & buffer,
       const page_type & page, const metadata_type & meta) const
{
    // ask the palette for the severity decoration
    auto severityColor = palette["severity"];
    // if we are generating color output
    if (!severityColor.empty()) {
        // print the application name in the correct color
        buffer
            << severityColor << meta.at("application") << palette["reset"];
    } else {
        // otherwise, print the application name, followed by the severity
        buffer
            << meta.at("application") << "(" << meta.at("severity") << ")";
    }

    // make some space, and print the first line of the body
    buffer
        << ": "
        << palette["body"] << page[0] << palette["reset"]
        << std::endl;

    // all done
    return;
}


void
pyre::journal::Alert::
body(palette_type & palette, buffer_type & buffer,
     const page_type & page, const metadata_type &) const
{
    // go through the lines in the page; skip the first one, since it was printed as part of
    // the header
    for (auto line = page.begin()+1; line != page.end(); ++line) {
        // and render them
        buffer
            << palette["body"] << (*line) << palette["reset"]
            << std::endl;
    }

    // all done
    return;
}


// end of file
