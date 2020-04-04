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


// metamethods
// destructor
pyre::journal::Stream::
~Stream()
{}


// interface
auto
pyre::journal::Stream::
memo(const page_type & page, const metadata_type & meta) -> Stream &
{
    // get the memo renderer to format the message
    auto content = _memo->render(_palette, page, meta);
    // inject it into my stream
    _stream << content;
    // all done
    return *this;
}


auto
pyre::journal::Stream::
alert(const page_type & page, const metadata_type & meta) -> Stream &
{
    // get the memo renderer to format the message
    auto content = _alert->render(_palette, page, meta);
    // inject it into my stream
    _stream << content;
    // all done
    return *this;
}


// end of file
