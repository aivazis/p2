// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2021 all rights reserved

// code guard
#if !defined(jcdev_forward_h)
#define jcdev_forward_h


// set up the namespace
namespace jcdev {
    // the custom renderer
    class Renderer;
    // the custom device
    class Device;
}


// user facing api
namespace jcdev {
    // the renderer
    using renderer_t = Renderer;
    // the custom device
    using device_t = Device;
}


#endif

// end of file
