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
       const page_type & page, const metadata_type & meta) const
{
    // if there is no contents
    if (page.empty()) {
        // we are done
        return;
    }

    // get the channel severity
    auto severity = meta.at("severity");

    // mark the beginning of a diagnostic
    bufmsg_type marker { " >> " };

    // attempt to get location information
    // N.B.: we only print line number and function name if we know the filename
    auto loc = meta.find("filename");
    // if it's there
    if (loc != meta.end()) {
        // extract the filename
        auto filename = loc->second;
        // make some room and turn on location formatting
        buffer << palette[severity];
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
            buffer << palette[severity] << line << palette["reset"] << ":";
        }

        // same with the function name
        auto & function = meta.at("function");
        // if we know it
        if (!function.empty()) {
            // render it
            buffer << palette[severity] << " " << function << palette["reset"] << ":";
        }
        // wrap up the location info
        buffer << std::endl;
    }

    // render the channel name and severity
    buffer
        // start things off with the marker
        << palette[severity] << marker << palette["reset"]
        // and the channel name
        << palette[severity] << meta.at("channel") << palette["reset"]
        // and the severity
        << " (" << palette[severity] << severity << palette["reset"] << ")"
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
            << palette[severity] << marker << palette["reset"]
            << palette[severity] << key << palette["reset"]
            << ": "
            << palette[severity] << value << palette["reset"]
            << std::endl;
    }

    // all done
    return;
}


void
pyre::journal::Memo::
body(palette_type & palette, buffer_type & buffer, const page_type & page,
     const metadata_type & meta) const
{
    // if the page is empty
    if (page.empty()) {
        // nothing to do
        return;
    }

    // make a marker
    bufmsg_type marker { " -- "  };
    // get the channel severity
    auto severity = meta.at("severity");

    // go through the lines in the page
    for (auto & line : page) {
        // and render them
        buffer
            << palette[severity] << marker << palette["reset"]
            << palette["body"] << line << palette["reset"]
            << std::endl;
    }

    // all done
    return;
}


// end of file
