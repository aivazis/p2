// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_api_h)
#define pyre_memory_api_h


// publish
namespace pyre::memory {
    // filemap
    using filemap_t = FileMap;
    // file-backed blocks of cells
    template <typename cellT> using map_t = Map<cellT>;
    template <typename cellT> using constmap_t = ConstMap<cellT>;
}


#endif

// end of file
