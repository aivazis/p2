// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_externals_h)
#define pyre_memory_externals_h


// standard library
#include <stdexcept>
#include <fstream>
#include <utility>

// low level stuff
#include <cstring>     // for {strerror}
#include <fcntl.h>     // for {open}
#include <unistd.h>    // for {close}
#include <sys/mman.h>  // for {mmap}
#include <sys/stat.h>  // for the mode flags

// support
#include <p2/journal.h>


// aliases that define implementation choices
namespace pyre::memory {
}


#endif

// end of file
