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
header(palette_type & palette, buffer_type & buffer,
       const page_type &, const metadata_type & meta) const
{
    // mark the beginning of a diagnostic
    bufmsg_type marker { " >> " };

    // attempt to get location information
    // N.B.: we only print line number and function name if we know the filename
    auto & filename = meta.at("filename");
    // if it's there
    if (!filename.empty()) {
        // make some room and turn on location formatting
        buffer << palette["filename"];
        // set a maximum length for the rendered filename
        const bufmsg_type::size_type maxlen = 60;
        // get the filename size
        auto len = filename.size();
        // so that names that are longer than this maximum
        if (len > maxlen) {
            // get shortened
            buffer
                << filename.substr(0, maxlen/4 - 3)
                << "..."
                << filename.substr(len - 3*maxlen/4);
        } else {
            // otherwise, render the whole name
            buffer << filename;
        }
        // reset the buffer and add a spacer
        buffer << palette["reset"] << ":";

        // attempt to get the line number
        auto & line = meta.at("line");
        // if we know it
        if (!line.empty()) {
            // render it
            buffer << palette["line"] << line << palette["reset"] << ":";
        }

        // same with the function name
        auto & function = meta.at("function");
        // if we know it
        if (!function.empty()) {
            // render it
            buffer << palette["function"] << " " << function << palette["reset"] << ":";
        }
        // wrap up the location info
        buffer << std::endl;
    }

    // render the channel name and severity
    buffer
        // start things off with the marker
        << marker
        // render the severity
        << palette["severity"] << meta.at("severity") << palette["reset"]
        // and the channel name
        << ": " << palette["channel"] << meta.at("channel") << palette["reset"]
        // done with the into line
        << std::endl;

    // now for the extra metadata, if any
    // build a set of the keys we have processed already
    std::set<key_type> known { "severity", "channel", "filename", "line", "function" };
    // go through the metadata
    for (auto & [key, value] : meta) {
        // if the key is in the known pile
        if (known.find(key) != known.end()) {
            // ignore it
            continue;
        }
        // otherwise, render it
        buffer
            << marker
            << palette["meta_key"] << key << palette["reset"]
            << ": "
            << palette["meta_value"] << value << palette["reset"]
            << std::endl;
    }

    // all done
    return;
}


void
pyre::journal::Memo::
body(palette_type & palette, buffer_type & buffer, const page_type & page,
     const metadata_type &) const
{
    // make a marker
    bufmsg_type marker { " -- "  };

    // go through the lines in the page
    for (auto & line : page) {
        // and render them
        buffer
            << marker << palette["body"] << line << palette["reset"]
            << std::endl;
    }

    // all done
    return;
}


// end of file
