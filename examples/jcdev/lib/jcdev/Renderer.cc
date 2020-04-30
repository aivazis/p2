// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the forward declarations
#include "forward.h"
// external support
#include "externals.h"
// my declaration
#include "Renderer.h"


// metamethods
jcdev::Renderer::
Renderer()
{}


jcdev::Renderer::
~Renderer()
{}


// implementation details
auto
jcdev::Renderer::
render(const entry_type & entry) const -> record_type
{
    // get the page
    auto page = entry.page();
    // and the notes
    auto notes = entry.notes();

    // the joiner
    auto join = [] (string_t buffer, const string_t & line) {
                    return std::move(buffer) + '\n' + line;
                };
    // assemble the message
    string_t message = std::accumulate(next(page.begin()), page.end(), page[0], join);

    // make a record
    record_type record
        {
         // add the severity
         notes.at("severity"),
         // the application
         notes.at("application"),
         // the channel name
         notes.at("channel"),
         // the filename
         notes.at("filename"),
         // the line number
         notes.at("line"),
         // the function name
         notes.at("function"),
         // the message
         message
    };

    // and yield it
    return record;
}


// end of file
