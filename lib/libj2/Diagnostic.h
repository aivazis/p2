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
    using string_type = std::string;
    using key_type = string_type;
    using value_type = string_type;

    using severity_type = severityT;

    // metamethods
public:
    inline Diagnostic();

    // interface
public:
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
