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
    template <typename T>
    using heap_t = Heap<T>;

    // file-backed blocks of cells
    template <typename T>
    using map_t = Map<T>;

    // file-backed blocks of const cells
    template <typename T>
    using constmap_t = ConstMap<T>;

    // view to someone else's data
    template <typename T>
    using view_t = View<T>;

    // const view to someone else's data
    template <typename T>
    using constview_t = ConstView<T>;
}


// low level entities; you should probably stay away from them
namespace pyre::memory {
    // support for managing file-backed memory undifferentiated blocks; this is the base class
    // for {map_t} and {constmap_t} above
    using filemap_t = FileMap;
}


#endif

// end of file
