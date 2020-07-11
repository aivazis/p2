// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_api_h)
#define pyre_memory_api_h


// user facing types
namespace pyre::memory {
    // block on the heap
    template <typename T, bool checkBounds = false>
    using heap_t = Heap<T, checkBounds>;

    // file-backed blocks of cells
    template <typename T, bool checkBounds = false>
    using map_t = Map<T, checkBounds>;

    // file-backed blocks of const cells
    template <typename T, bool checkBounds = false>
    using constmap_t = ConstMap<T, checkBounds>;

    // view to someone else's data
    template <typename T, bool checkBounds = false>
    using view_t = View<T, checkBounds>;

    // const view to someone else's data
    template <typename T, bool checkBounds = false>
    using constview_t = ConstView<T, checkBounds>;
}


// low level entities; you should probably stay away from them
namespace pyre::memory {
    // support for managing file-backed memory undifferentiated blocks; this is the base class
    // for {map_t} and {constmap_t} above
    using filemap_t = FileMap;
}


#endif

// end of file
