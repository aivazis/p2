// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_forward_h)
#define pyre_journal_forward_h


// forward declarations of all user facing entities
namespace pyre::journal {
    // the exceptions
    class firewall_error;

    // infrastructure
    template <typename> class Index;
    template <bool = true> class Inventory;
    template <typename severityT> class Channel;
    class Chronicler;

    // devices
    class Device;
    class Trash;
    class Stream;
    class Console;

    // the null diagnostic
    class Null;
    // its injection operator
    template <typename itemT>
    inline auto operator<< (const Null &, const itemT &) -> const Null &;
    // its manipulators
    inline auto endl(const Null &) -> const Null &;
    inline auto newline(const Null &) -> const Null &;

    // locator
    class Locator;
    // manipulators
    class Selector;
}

// low level api
#if defined(PYRE_CORE)
namespace pyre::journal {
    // infrastructure
    template <typename inventoryT>
    using index_t = Index<inventoryT>;

    template <bool stateV = true>
    using inventory_t = Inventory<stateV>;

    template <typename severityT>
    using channel_t = Channel<severityT>;

    using chronicler_t = Chronicler;
}
#endif


// developer api
namespace pyre::journal {
    // the null diagnostic is always available
    using null_t = Null;

    // if we are building the library
#if defined(PYRE_CORE)
    // enable the developer channels
    // using debug_t = Debug;
    // using firewall_t = Firewall;

    // if the user has explicitly requested no debugging
#elif defined(NDEBUG)
    // disable the developer channels
    using debug_t = Null;
    using firewall_t = Null;

    // if the user has explicitly asked for debugging support
#elif defined(DEBUG) || defined(JOURNAL_DEBUG)
    // enable the developer channels
    // using debug_t = Debug;
    // using firewall_t = Firewall;

    // otherwise, assume this is a production build
#else
    // disable the developer channels
    using debug_t = Null;
    using firewall_t = Null;
#endif
}


// user facing api
namespace pyre::journal {
    // infrastructure
    // devices
    using device_t = Device;
    using trash_t = Trash;
    using stream_t = Stream;
    using console_t = Console;

    // channels
    // using error_t = Error;
    // using info_t = Informational;
    // using warning_t = Warning;

    // manipulators
     using at = Locator;
     using set = Selector;
}


#endif

// end of file
