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
render(const page_type & page, const metadata_type & meta) const -> record_type
{
    // make a record
    record_type record;

    // add the severity
    record.push_back(meta.at("severity"));
    // the application
    record.push_back(meta.at("application"));
    // the channel name
    record.push_back(meta.at("channel"));
    // the filename
    record.push_back(meta.at("filename"));
    // the line number
    record.push_back(meta.at("line"));
    // the function name
    record.push_back(meta.at("function"));

    // the joiner
    auto join = [] (string_t buffer, const string_t & line) {
                    return std::move(buffer) + '\n' + line;
                };
    // assemble the message
    string_t message = std::accumulate(next(page.begin()), page.end(), page[0], join);

    // and add it to the pile
    record.push_back(message);

    // all done
    return record;
}


// end of file
