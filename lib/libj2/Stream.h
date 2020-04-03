// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Stream_h)
#define pyre_journal_Stream_h


// a device that writes to output streams
class pyre::journal::Stream : public pyre::journal::Device {
    // types
public:
    using stream_type = outputstream_t;
    using renderer_type = Renderer;
    using renderer_pointer = Renderer::pointer_type;

    // metamethods
public:
    // constructor
    inline explicit Stream(const name_type &, stream_type &);
    // destructor
    virtual ~Stream();

    // interface
public:
    // developer diagnostics
    virtual auto memo(const page_type &, const metadata_type &) -> Stream &;
    // user facing diagnostics
    virtual auto alert(const page_type &, const metadata_type &) -> Stream &;

    // data
private:
    // the stream to write to
    stream_type & _stream;
    // the renderer for memos
    renderer_pointer _memo;
    // the renderer for alerts
    renderer_pointer _alert;
};


// get the inline definitions
#define pyre_journal_Stream_icc
#include "Stream.icc"
#undef pyre_journal_Stream_icc


#endif

// end of file
