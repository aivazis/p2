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
// renderer support
#include "Renderer.h"
#include "Memo.h"
#include "Alert.h"

// get the device declaration
#include "Device.h"
// get the stream declaration
#include "Stream.h"
// get the manager of the global state
#include "Chronicler.h"


// metamethods
// destructor
pyre::journal::Stream::
~Stream()
{}


// interface
auto
pyre::journal::Stream::
memo(verbosity_type verbosity, const page_type & page, const metadata_type & meta) -> Stream &
{
    // get the verbosity level
    auto maxVerbosity = chronicler_t::verbosity();
    // if this message is chattier
    if (verbosity > maxVerbosity) {
        // do nothing
        return *this;
    }
    // otherwise, get the memo renderer to format the message
    auto content = _memo->render(_palette, page, meta);
    // inject it into my stream
    _stream << content;
    // all done
    return *this;
}


auto
pyre::journal::Stream::
alert(verbosity_type verbosity, const page_type & page, const metadata_type & meta) -> Stream &
{
    // get the verbosity level
    auto maxVerbosity = chronicler_t::verbosity();
    // if this message is chattier
    if (verbosity > maxVerbosity) {
        // do nothing
        return *this;
    }
    // otherwise, get the alert renderer to format the message
    auto content = _alert->render(_palette, page, meta);
    // inject it into my stream
    _stream << content;
    // all done
    return *this;
}


// end of file
