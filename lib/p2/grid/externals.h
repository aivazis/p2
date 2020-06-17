// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_externals_h)
#define pyre_grid_externals_h


// externals
#include <array>
#include <numeric>
#include <ostream>

// support
#include <p2/journal.h>
#include <p2/memory.h>


// aliases that define implementation choices
namespace pyre::grid {
    // make sure we are on the same page as {memory} on these fundamental types
    // sizes of things
    using size_t = pyre::memory::size_t;
    // strings
    using string_t = pyre::memory::string_t;
    // names of things
    using name_t = pyre::memory::name_t;
    // filenames
    using uri_t = pyre::memory::uri_t;

    // arrays of things
    template <typename T, size_t N>
    using array_t = std::array<T, N>;

    // output streams
    using ostream_t = std::ostream;
    using ostream_reference = std::ostream &;
}


#endif

// end of file
