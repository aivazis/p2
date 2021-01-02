// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2021 all rights reserved


// external dependnecies
#include "externals.h"
// get the local declarations
#include "forward.h"
// implementations
#include "Renderer.h"
#include "Device.h"


// metamethods
jcdev::Device::
~Device()
{}


// record a developer facing message
auto
jcdev::Device::
memo(const entry_type & entry) -> Device &
{
    // render and inject the message
    inject(entry);
    // all done
    return *this;
}


// record a user facing message
auto
jcdev::Device::
alert(const entry_type & entry) -> Device &
{
    // render and inject the message
    inject(entry);
    // all done
    return *this;
}


// the workhorse
void
jcdev::Device::
inject(const entry_type & entry)
{
    // get the time
    std::time_t now = std::time(nullptr);
    // inject the timestamp
    _stream << '"' << std::put_time(std::localtime(&now), "%F %T %z") << '"';

    // render
    record_type record { _renderer.render(entry) };
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
