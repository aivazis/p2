// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_externals_h)
#define pyre_journal_externals_h


// externals
#include <cstdlib>
#include <type_traits>
#include <stdexcept>
#include <utility>
#include <memory>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <ostream>
#include <sstream>
#include <iomanip>


// aliases for fundamental types that define implementation choices
namespace pyre::journal {
    // strings
    using string_t = std::string;
    // output stream; careful here: we already have a {stream_t} that points to {Stream}
    using outputstream_t = std::ostream;

    // generic names
    using name_t = string_t;

    // a set of generic names
    using nameset_t = std::set<name_t>;

    // a page is the payload of a journal entry
    using page_t = std::vector<string_t>;
    // the metadata associated with an journal entry
    using key_t = string_t;
    using value_t = string_t;
    using metadata_t = std::map<key_t, value_t>;

    // support for message buffering; unfortunately {std::stringstream} doesn't expose the
    // return type of its {str} method, so i need a redundant definition here
    using bufmsg_t = string_t;
    using buffer_t = std::stringstream;

    // a color table is a map from a color name to a control string
    using colorname_t = string_t;
    using colorrep_t = string_t;
    using colortable_t = std::map<colorname_t, colorrep_t>;

    // a palette is a map from e metadata key to a color name
    using palette_t = std::map<key_t, colorrep_t>;
}


#endif

// end of file
