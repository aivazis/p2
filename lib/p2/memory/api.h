// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_api_h)
#define pyre_memory_api_h


// user facing types
namespace pyre::memory {
    // file-backed blocks of cells
    template <typename cellT, bool checkBounds = false>
    using map_t = Map<cellT, checkBounds>;

    // file-backed blocks of const cells
    template <typename cellT, bool checkBounds = false>
    using constmap_t = ConstMap<cellT, checkBounds>;

    // view to someone else's data
    template <typename cellT, bool checkBounds = false>
    using view_t = View<cellT, checkBounds>;

    // const view to someone else's data
    template <typename cellT, bool checkBounds = false>
    using constview_t = ConstView<cellT, checkBounds>;
}


// low level entities; you should probably stay away from them
namespace pyre::memory {
    // support for managing file-backed memory undifferentiated blocks; this is the base class
    // for {map_t} and {constmap_t} above
    using filemap_t = FileMap;
}


#endif

// end of file
