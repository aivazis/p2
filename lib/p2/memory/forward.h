// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_forward_h)
#define pyre_memory_forward_h


// set up the namespace
namespace pyre::memory {
    // file-backed block of undifferentiated memory
    class FileMap;

    // file-backed block of cells
    template <typename cellT, bool checkBounds> class Map;
    // file-backed block of const cells
    template <typename cellT, bool checkBounds> class ConstMap;
};


#endif

// end of file
