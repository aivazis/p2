// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(jcdev_externals_h)
#define jcdev_externals_h


// standard library
#include <ctime>
#include <vector>
#include <numeric>
#include <ostream>
#include <iomanip>
// get the journal
#include <p2/journal.h>


// aliases for fundamental types that define implementation choices
namespace jcdev {
    // sizes of things
    using size_t = std::size_t;
    // strings
    using string_t = std::string;

    // a csv record
    using record_t = std::vector<string_t>;
}


#endif

// end of file
