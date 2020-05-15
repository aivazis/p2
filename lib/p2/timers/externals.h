// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_timers_externals_h)
#define pyre_timers_externals_h


// externals
#include <type_traits>
#include <stdexcept>
#include <utility>
#include <chrono>
#include <memory>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <filesystem>


// aliases for fundamental types that define implementation choices
namespace pyre::timers {
    // sizes of things
    using size_t = std::size_t;
    // strings
    using string_t = std::string;
    // paths
    using path_t = std::filesystem::path;
    // scratch buffers
    using buffer_t = std::stringstream;

    // the clock
    using clock_t = std::chrono::steady_clock;

    // seconds
    using seconds_t = std::chrono::duration<double>;
    using milliseconds_t = std::chrono::duration<double, std::milli>;
    using microseconds_t = std::chrono::duration<double, std::micro>;

    // generic names
    using name_t = string_t;
    // set of names
    using nameset_t = std::set<name_t>;

    // command line parsing
    using cmdname_t = string_t;
    using cmdvalue_t = string_t;
    using cmd_t = std::map<cmdname_t, cmdvalue_t>;
}


#endif

// end of file
