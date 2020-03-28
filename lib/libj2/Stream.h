// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Stream_h)
#define pyre_journal_Stream_h

//
class pyre::journal::Stream : public pyre::journal::device_t {
    // types
public:
    using stream_type = std::ostream;

    // metamethods
public:
    // constructor
    inline explicit Stream(const name_type &, stream_type &);
    // destructor
    virtual ~Stream();

    // interface
public:
    // abstract
    virtual auto record(const entry_type &, const metadata_type &) -> Stream &;

    // data
private:
    stream_type & _stream;
};


// get the inline definitions
#define pyre_journal_Stream_icc
#include "Stream.icc"
#undef pyre_journal_Stream_icc


#endif

// end of file
