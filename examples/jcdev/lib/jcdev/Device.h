// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2021 all rights reserved

// code guard
#if !defined(jcdev_Device_h)
#define jcdev_Device_h


// custom device
class jcdev::Device : public pyre::journal::Device {
    // types
public:
    // inherit whatever the journal uses as output streams
    using stream_type = pyre::journal::outputstream_t;
    // my renderer
    using renderer_type = Renderer;
    // its record type
    using record_type = Renderer::record_type;

    // metamethods
public:
    virtual ~Device();
    inline Device(stream_type & stream);

    // interface
public:
    // developer diagnostics
    virtual auto memo(const entry_type &) -> Device &;
    // user facing diagnostics
    virtual auto alert(const entry_type &) -> Device &;


    // implementation details
protected:
    virtual void inject(const entry_type &);

    // data members
private:
    // the stream to write to
    stream_type & _stream;
    // the renderer
    renderer_type _renderer;
};


// get the inline definitions
#define jcdev_Device_icc
#include "Device.icc"
#undef jcdev_Device_icc


#endif

// end of file
