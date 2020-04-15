// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// external dependnecies
#include "externals.h"
// get the local declarations
#include "forward.h"
// implementations
#include "Renderer.h"
#include "Device.h"


// record a developer facing message
auto
jcdev::Device::
memo(verbosity_type verbosity, const page_type & page, const metadata_type & meta) -> Device &
{
    // render and inject the message
    inject(verbosity, page, meta);
    // all done
    return *this;
}


// record a user facing message
auto
jcdev::Device::
alert(verbosity_type verbosity, const page_type & page, const metadata_type & meta) -> Device &
{
    // render and inject the message
    inject(verbosity, page, meta);
    // all done
    return *this;
}


// the workhorse
void
jcdev::Device::
inject(verbosity_type verbosity, const page_type & page, const metadata_type & meta)
{
    // get the time
    std::time_t now = std::time_t(nullptr);
    // inject the timestamp
    _stream << '"' << std::put_time(std::localtime(&now), "%F %T %z") << '"';

    // render
    record_type record { _renderer.render(page, meta) };
    // go through the entries
    for (const auto & line : record) {
        // and inject each one
        _stream << "," << std::quoted(line);
    }

    // flush
    _stream << std::endl;

    // all done
    return;
}


// end of file
