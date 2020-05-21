// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// externals
#include "externals.h"
// forward declarations
#include "forward.h"
// type aliases
#include "api.h"

// my class declaration
#include "FileMap.h"


pyre::memory::FileMap::
FileMap(uri_type uri, writable_type writable,
        size_type bytes, offset_type offset, preserve_type preserve):
    _uri { uri },
    _info {},
    _bytes { bytes },
    _buffer { nullptr }

{
    // make a channel
    journal::debug_t channel("pyre.memory.map");

    // all done
    return;
}


// end of file
