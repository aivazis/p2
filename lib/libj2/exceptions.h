// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_exceptions_h)
#define pyre_journal_exceptions_h


// exception raised by firewalls
class pyre::journal::firewall_error : public std::logic_error {
    // types
public:
    using string_t = std::string;

    // metamethods
public:
    firewall_error(const string_t &);
    firewall_error(const char *);
};


// get the inline definitions
#define pyre_journal_exceptions_icc
#include "exceptions.icc"
#undef pyre_journal_exceptions_icc


#endif

// end of file