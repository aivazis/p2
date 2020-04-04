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
    // surely this is useful somewhere...
    using string_type = string_t;
    // conversion to an {ostream} so standard manipulators can work
    using ostream_type = outputstream_t;
    // diagnostic payload
    using page_type = page_t;
    // diagnostic metadata
    using key_type = key_t;
    using value_type = value_t;
    using metadata_type = metadata_t;
    // message buffering
    using bufmsg_type = bufmsg_t;
    using buffer_type = buffer_t;

    // metamethods
public:
    inline Diagnostic();

    // interface
public:
    // accessors
    inline auto buffer() -> bufmsg_type;
    inline auto page() const -> const page_type &;
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
    page_type _page;
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
