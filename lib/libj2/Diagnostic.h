// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Diagnostic_h)
#define pyre_journal_Diagnostic_h


// support for injecting and recording information in channels
template <typename severityT>
class pyre::journal::Diagnostic {
    // types
public:
    using severity_type = severityT;

    using string_type = std::string;
    using ostream_type = std::ostream;

    using key_type = string_type;
    using value_type = string_type;

    using buffer_type = std::stringstream;
    using entry_type = std::vector<string_type>;
    using metadata_type = std::map<string_type, string_type>;

    // metamethods
public:
    inline Diagnostic();

    // interface
public:
    // accessors
    inline auto buffer() -> string_type;
    inline auto entry() const -> const entry_type &;
    inline auto metadata() const -> const metadata_type &;

    // conversion to an {ostream}
    inline operator ostream_type & ();

    // end of transaction
    inline auto record() -> Diagnostic &;
    // new line
    inline auto newline() -> Diagnostic &;
    // decoration by metadata
    auto setattr(const key_type &, const value_type &) -> Diagnostic &;
    // item injection
    template <typename itemT>
    inline auto inject(const itemT &) -> Diagnostic &;

    // data members
private:
    entry_type _entry;
    buffer_type _buffer;
    metadata_type _metadata;

    // disallow
private:
    Diagnostic(const Diagnostic &) = delete;
    Diagnostic(const Diagnostic &&) = delete;
    const Diagnostic & operator=(const Diagnostic &) = delete;
    const Diagnostic & operator=(const Diagnostic &&) = delete;
};


// get the inline definitions
#define pyre_journal_Diagnostic_icc
#include "Diagnostic.icc"
#undef pyre_journal_Diagnostic_icc


#endif

// end of file
